from basisklassen import FrontWheels, BackWheels, Ultrasonic, Infrared
from soniccar import SonicCar
from sensorcar import SensorCar
import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import ast
import plotly.express as px
import  os
from fahrmodus import Fahrmodus


#Auto erstellen
fw = FrontWheels()
bw = BackWheels() 
usm = Ultrasonic()
sc = SonicCar(fw, bw, ultra=usm)
ir = Infrared()
sensor_c = SensorCar(fw, bw, ultra=usm, infra=ir)
fm = Fahrmodus(sensor_c)

# Initialdaten laden
if os.path.exists("sonic_log.csv"):
    df = pd.read_csv('sonic_log.csv', delimiter=',')
# else:
#     df = DataFrame({
#         "UTCtime":[0],
#         "timestamp":[0],
#         "speed":[0],
#         "steering_angle":[0]
#     })



# Funktion zur Berechnung der KPIs
def calculate_kpis(df):
    max_speed = (df['speed'].max())*0.2778
    #?? negative Geschwindigkeit
    min_speed = (df['speed'].min())*0.2778
    avg_speed = (df['speed'].abs().mean())*0.2778
    avg_speed_fl =  avg_speed.item() 
    total_time = df['UTCtime'].max() - df['UTCtime'].min()
    total_time_sec = total_time.item()
    print(total_time_sec)
    #?? str und runden
    total_time_str = str(timedelta(seconds=total_time))
    print(total_time_str)
    total_distance_calculation = avg_speed_fl * total_time_sec
    return max_speed, min_speed, avg_speed, total_time_sec, total_distance_calculation

max_speed, min_speed, avg_speed, total_time_sec, total_distance_calculation = calculate_kpis(df)

df['time'] = pd.to_datetime(df['UTCtime'], unit='s')
fig = px.line(df, x='time', y='speed', title='Geschwindigkeit über Zeit',
              labels={'time': 'Zeit', 'speed': 'Geschwindigkeit (cm/s)'},
              template='plotly_dark')
fig_2 = px.line(df, x='time', y='steering_angle', title='Lenkwinkel über Zeit',
              labels={'time': 'Zeit', 'steering_angle': 'Lenkwinkel (°)'},
              template='plotly_dark')

# URL zum Bootstrap 5.3 Stylesheet – ermöglicht die Nutzung von Bootstrap-Klassen wie 'btn', 'row', 'col', 'text-center' usw.
BOOTSTRAP = "https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css"
 
# Dash-App mit eingebundenem Bootstrap-Stylesheet initialisieren
app = dash.Dash(__name__, external_stylesheets=[BOOTSTRAP])
 
app.layout = dbc.Container([
    html.H1("🚗 Car Telemetry Dashboard", className="text-center my-4 text-info"),
    
       # Dropdown + Button
    dbc.Row([
        dbc.Col(dbc.Card(dbc.CardBody([
            html.H4("Fahrmodus auswählen"),
            dcc.Dropdown(
                id='mode-dropdown',
                options=[
                    {'label': 'Fahrmodus 1', 'value': 1},                    
                    {'label': 'Fahrmodus 2', 'value': 2},
                    {'label': 'Fahrmodus 3', 'value': 3},
                    {'label': 'Fahrmodus 4', 'value': 4},
                    {'label': 'Fahrmodus 5', 'value': 5},
                    {'label': 'Fahrmodus 6', 'value': 6},
                    {'label': 'Fahrmodus 7', 'value': 7},
                    {'label': 'Fahrmodus 8', 'value': 8}
                ],
                value=4,
                clearable=False,
                className="mb-3"
            ),
            dbc.Button("Starten", id="start-button", color="primary", className="mt-3")
        ])), width=12)
    ], className="gy-4"),
 
    # KPI-Karten
    dbc.Row([
        dbc.Col(dbc.Card(dbc.CardBody([
            html.H4("🏁 Max Speed"), html.H2(id="max-speed", children=f"{max_speed} cm/s")
        ])), width=2),
        dbc.Col(dbc.Card(dbc.CardBody([
            html.H4("🐢 Min Speed"), html.H2(id="min-speed", children=f"{min_speed} cm/s")
        ])), width=2),
        dbc.Col(dbc.Card(dbc.CardBody([
            html.H4("⚖️ Avg Speed"), html.H2(id="avg-speed", children=f"{avg_speed:.2f} cm/s")
        ])), width=2),
        dbc.Col(dbc.Card(dbc.CardBody([
            html.H4("🗺️ Total distance"), html.H2(id="total-distance", children=f"{total_distance_calculation:.2f} cm")
        ])), width=2),
        dbc.Col(dbc.Card(dbc.CardBody([
            html.H4("⏱️ Total Time"), html.H2(id="total-time", children=f"{total_time_sec:.2f} sec")
        ])), width=2),
    ], className="gy-4", style={
        'display': 'flex',
        'flexWrap': 'wrap',
        'justifyContent': 'center',
        'gap': '20px'}),  
     
    # Diagramm
    dbc.Row([
        dbc.Col(dbc.Card(dbc.CardBody([
            dcc.Graph(id="speed-graph", figure=fig)
        ])), width=12)
    ], className="gy-4"), 

    dbc.Row([
        dbc.Col(dbc.Card(dbc.CardBody([
            dcc.Graph(id="steering_angle_graph", figure=fig_2)
        ])), width=12)
    ], className="gy-4")
], fluid=True)
 
# Callback zur Ausführung des Fahrmodus und Aktualisierung
@app.callback(
    Output('max-speed', 'children'),
    Output('min-speed', 'children'),
    Output('avg-speed', 'children'),
    Output('total-time', 'children'),
    Output('total-distance', 'children'),
    Output('speed-graph', 'figure'),
    Input('start-button', 'n_clicks'),
    State('mode-dropdown', 'value')
)

#reihenfolge muss mit Input übereinstimmen
def update_dashboard(n_clicks, mode):
    if n_clicks is None:
       # return dash.no_update,"","","",""
       return dash.no_update
  
    # Fahrmodus ausführen
    #subprocess.run(["python3", "carmain.py"])
    fm.user_selected_mode(mode)

    # Neue Daten laden
    df = pd.read_csv('sonic_log.csv', delimiter=',')
    max_speed, min_speed, avg_speed, total_time_sec, total_distance_calculation = calculate_kpis(df)
    df['time'] = pd.to_datetime(df['UTCtime'], unit='s')
    fig = px.line(df, x='time', y='speed', title='Geschwindigkeit über Zeit',
                labels={'time': 'Zeit', 'speed': 'Geschwindigkeit  cm/s)'},
                template='plotly_dark')
    fig_2 = px.line(df, x='time', y='steering_angle', title='Lenkwinkel über Zeit',
              labels={'time': 'Zeit', 'steering_angle': 'Lenkwinkel (°)'},
              template='plotly_dark')

    return f"{max_speed} cm/s", f"{min_speed} cm/s", f"{avg_speed:.2f} cm/s", f"{total_time_sec:.2f} sek", f"{total_distance_calculation:.2f} cm", fig, fig_2
 
if __name__ == '__main__':
    app.run(debug=True)