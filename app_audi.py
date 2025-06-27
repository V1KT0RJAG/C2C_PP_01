from basisklassen import FrontWheels, BackWheels, Ultrasonic, Infrared
from soniccar import SonicCar
from sensorcar import SensorCar
import dash
from dash import dcc, html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output
import pandas as pd
from datetime import datetime
import ast
import plotly.express as px
import subprocess
from datetime import timedelta
import  os
from fahrmodus import Fahrmodus


#Auto erstellen
fw = FrontWheels()
bw = BackWheels() 
usm = Ultrasonic()
sc = SonicCar(fw, bw, ultra=usm)
ir = Infrared()
sensor_c = SensorCar(fw, bw, ultra=usm, infra=ir)
fm = Fahrmodus(sc)

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
    max_speed = df['speed'].max()
    #?? negative Geschwindigkeit
    min_speed = df['speed'].min()
    avg_speed = abs(df['speed'].mean())
    total_time = df['UTCtime'].max() - df['UTCtime'].min()
    #?? str und runden
    total_time_str = str(timedelta(seconds=total_time))
    return max_speed, min_speed, avg_speed, total_time_str
 

max_speed, min_speed, avg_speed, total_time_str = calculate_kpis(df)
df['time'] = pd.to_datetime(df['UTCtime'], unit='s')
fig = px.line(df, x='time', y='speed', title='Geschwindigkeit über Zeit',
              labels={'time': 'Zeit', 'speed': 'Geschwindigkeit (km/h)'},
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
                    {'label': 'Fahrmodus 4', 'value': 4}
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
            html.H4("🏁 Max Speed"), html.H2(id="max-speed", children=f"{max_speed} km/h")
        ])), width=3),
        dbc.Col(dbc.Card(dbc.CardBody([
            html.H4("🐢 Min Speed"), html.H2(id="min-speed", children=f"{min_speed} km/h")
        ])), width=3),
        dbc.Col(dbc.Card(dbc.CardBody([
            html.H4("⚖️ Avg Speed"), html.H2(id="avg-speed", children=f"{avg_speed:.2f} km/h")
        ])), width=3),
        # dbc.Col(dbc.Card(dbc.CardBody([
        #     html.H4("🗺️ Total distance"), html.H2(id="total-distance", children=total_distance)
        # ])), width=3),
        dbc.Col(dbc.Card(dbc.CardBody([
            html.H4("⏱️ Total Time"), html.H2(id="total-time", children=total_time_str)
        ])), width=3),
    ], className="gy-4"),
 
    # Diagramm
    dbc.Row([
        dbc.Col(dbc.Card(dbc.CardBody([
            dcc.Graph(id="speed-graph", figure=fig)
        ])), width=12)
    ], className="gy-4")
], fluid=True)
 
# Callback zur Ausführung des Fahrmodus und Aktualisierung
@app.callback(
    Output('max-speed', 'children'),
    Output('min-speed', 'children'),
    Output('avg-speed', 'children'),
    Output('total-time', 'children'),
    #  Output('total-distance', 'children'),
    Output('speed-graph', 'figure'),
    Input('start-button', 'n_clicks'),
    Input('mode-dropdown', 'value')
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
    max_speed, min_speed, avg_speed, total_time_str = calculate_kpis(df)
    df['time'] = pd.to_datetime(df['UTCtime'], unit='s')
    fig = px.line(df, x='time', y='speed', title='Geschwindigkeit über Zeit',
                  labels={'time': 'Zeit', 'speed': 'Geschwindigkeit (km/h)'},
                  template='plotly_dark')
 
    return f"{max_speed} km/h", f"{min_speed} km/h", f"{avg_speed:.2f} km/h", total_time_str, fig
 
if __name__ == '__main__':
    app.run(debug=True)