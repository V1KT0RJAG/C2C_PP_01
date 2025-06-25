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

# Funktion zum Einlesen der Logdatei
# def read_logfile():
#     logfile_path = "fahrprotokoll.log"
#     data = []
#     with open(logfile_path, "r") as file:
#         for line in file:
#             try:
#                 entry = ast.literal_eval(line.strip())
#                 data.append(entry)
#             except Exception as e:
#                 print(f"Fehler beim Parsen der Zeile: {line} – {e}")
#     return pd.DataFrame(data)



# Funktion zur Berechnung der KPIs
def calculate_kpis(df):
    max_speed = df['speed'].max()
    #?? negative Geschwindigkeit
    min_speed = df['speed'].min()
    avg_speed = abs(df['speed'].mean())
    total_time = df['timestamp'].max() - df['timestamp'].min()
    #?? str und runden
    total_time_str = str(timedelta(seconds=total_time))
    return max_speed, min_speed, avg_speed, total_time_str
 
# Initialdaten laden
df = pd.read_csv('sonic_log_good_data.csv', delimiter=',')
 
max_speed, min_speed, avg_speed, total_time_str = calculate_kpis(df)
df['time'] = pd.to_datetime(df['timestamp'], unit='s')
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
    [Output('max-speed', 'children'),
     Output('min-speed', 'children'),
     Output('avg-speed', 'children'),
     Output('total-time', 'children'),
     Output('speed-graph', 'figure')],
    [Input('start-button', 'n_clicks')],
    [Input('mode-dropdown', 'value')]
)
def update_dashboard(n_clicks, mode):
    if n_clicks is None:
        return dash.no_update
 
    # Fahrmodus ausführen
    subprocess.run(["python3", "test_soniccar.py", str(mode)])
 
    # Neue Daten laden
    df = pd.read_csv('sonic_log_good_data.csv', delimiter=',')
    max_speed, min_speed, avg_speed, total_time_str = calculate_kpis(df)
    df['time'] = pd.to_datetime(df['timestamp'], unit='s')
    fig = px.line(df, x='time', y='speed', title='Geschwindigkeit über Zeit',
                  labels={'time': 'Zeit', 'speed': 'Geschwindigkeit (km/h)'},
                  template='plotly_dark')
 
    return f"{max_speed} km/h", f"{min_speed} km/h", f"{avg_speed:.2f} km/h", total_time_str, fig
 
if __name__ == '__main__':
    app.run(debug=True)