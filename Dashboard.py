import dash
from dash import html, dcc, Dash, Input, Output
import dash_bootstrap_components as dbc
import random

import pandas as pd
import plotly.express as px
from datetime import datetime

from basecar import BaseCar
from fahrmodus import Fahrmodus
from soniccar import SonicCar
from basisklassen import FrontWheels, BackWheels, Ultrasonic

# Initialisierung
fw = FrontWheels()
bw = BackWheels()
usm = Ultrasonic()
sc = SonicCar(fw, bw, usm)

fahrmodus = Fahrmodus(sc)


# Daten lesen graph bauen
timestamp_data = datetime.now().strftime('%Y-%m-%d') #Zeitstempel für den Dateinamen
df = pd.read_csv(f"Loggdata_{timestamp_data}.csv")
figGeschw = px.line(df, x="Timestamp", y="Speed", title="Geschwindigkeitsverlauf")
figLenk = px.line(df, x="Timestamp", y="Lenkwinkel", title="Lenkwinkelverlauf")
figUltra = px.line(df, x="Timestamp", y="Ultraschallsensor", title="Ultraschallsensorverlauf")   

# # min max mean ausrechen
maxspeed = df["Speed"].max()
minspeed = df["Speed"].min()
meanspeed = round(df["Speed"].mean(),2)    




# Dash App starten
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.MORPH])

# Layout der App
app.layout = html.Div(children=[
    
    # Titelzeile
    dbc.Row([
        dbc.Col([html.H1('Fahrzeug Dashboard Gruppe 2', style={'textAlign': 'center'})])
    ], align='center'),

    # Kachelanzeige
    dbc.Row([
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H4("Minimale Geschwindigkeit", className="card-title"),
                    html.P(f"{minspeed} km/h", className="card-text")
                ]), className="mb-4", color="primary", inverse=True
            ), width=4
        ),
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H4("Durchschnitt Geschwindigkeit", className="card-title"),
                    html.P(f"{meanspeed} km/h", className="card-text")
                ]), className="mb-4", color="success", inverse=True
            ), width=4
        ),
        dbc.Col(
            dbc.Card(
                dbc.CardBody([
                    html.H4("Maximale Geschwindigkeit", className="card-title"),
                    html.P(f"{maxspeed} km/h", className="card-text")
                ]), className="mb-4", color="primary", inverse=True
            ), width=4
        ),
    ]),

    # Fahrmodus Buttons
    html.Hr(),
    html.H4("Fahrmodi starten"),
    dbc.Row([
        dbc.Col(dbc.Button("Fahrmodus 1: Vorwärts und Rückwärts", id="btn-modus-1", color="primary", className="mb-2"), width=3),
        dbc.Col(dbc.Button("Fahrmodus 2: Kreisfahrt", id="btn-modus-2", color="secondary", className="mb-2"), width=3),
        dbc.Col(dbc.Button("Fahrmodus 3: Vorwärts bis Hindernis", id="btn-modus-3", color="success", className="mb-2"), width=3),
        dbc.Col(dbc.Button("Fahrmodus 4: Erkundungstour", id="btn-modus-4", color="warning", className="mb-2"), width=3),

    ]),
    html.Div(id="output-modus", className="mt-3", style={"fontWeight": "bold"}),
    
   dbc.Row([
        dbc.Col([dcc.Graph(id="Geschwindigkeitsverlauf", figure=figGeschw)]),
        dbc.Col([dcc.Graph(id="Lenkwinkel", figure=figLenk)]),
        dbc.Col([dcc.Graph(id="Ultraschallsensor", figure=figUltra)]),
        dbc.Col(dbc.Button("Graph aktualisieren", id="btn-modus-5", color="warning", className="mb-2"), width=3) 
   ])   
    
])

# Callback zur Buttonverarbeitung
@app.callback(
    Output("output-modus", "children"),
    Input("btn-modus-1", "n_clicks"),
    Input("btn-modus-2", "n_clicks"),
    Input("btn-modus-3", "n_clicks"),
    Input("btn-modus-4", "n_clicks")
)
def starte_fahrmodus(n1, n2, n3, n4):
    ctx = dash.callback_context


    button_id = ctx.triggered[0]["prop_id"].split(".")[0]

    try:
        if button_id == "btn-modus-1":
            fahrmodus.fahrmodus_1()
            return "Fahrmodus 1 wurde ausgeführt."
        elif button_id == "btn-modus-2":
            fahrmodus.fahrmodus_2()
            return "Fahrmodus 2 wurde ausgeführt."
        elif button_id == "btn-modus-3":
            fahrmodus.fahrmodus_3()
            return "Fahrmodus 3 wurde ausgeführt."
        elif button_id == "btn-modus-4":
            fahrmodus.fahrmodus_4()
            return "Fahrmodus 4 wurde ausgeführt."
    except Exception as e:
        return f"Fehler beim Ausführen: {str(e)}"
    
@app.callback(
    Output('Geschwindigkeitsverlauf', 'figure'),
    Output('Lenkwinkel', 'figure'),
    Output('Ultraschallsensor', 'figure'),
    Input('btn-modus-5', 'n_clicks')
)

def update_graph(n5):
    ctx = dash.callback_context
    button_id = ctx.triggered[0]["prop_id"].split(".")[0]
    timestamp_data = datetime.now().strftime('%Y-%m-%d')
    try:
        if button_id == "btn-modus-5":  # ← Hier war der Fehler!
            df = pd.read_csv(f"Loggdata_{timestamp_data}.csv")

            figGeschw = px.line(df, x="Timestamp", y="Speed", title="Geschwindigkeitsverlauf")
            figLenk = px.line(df, x="Timestamp", y="Lenkwinkel", title="Lenkwinkelverlauf")
            figUltra = px.line(df, x="Timestamp", y="Ultraschallsensor", title="Ultraschallsensorverlauf")

            return figGeschw, figLenk, figUltra

    except FileNotFoundError:
        empty_fig = px.line(title="Keine Daten verfügbar")
        return empty_fig, empty_fig, empty_fig
       
    
    
    
    
    


# App starten (nur bei direktem Start)
if __name__ == "__main__":
    app.run_server(debug=True)
