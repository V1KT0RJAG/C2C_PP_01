from dash import html, Dash, dcc, Input, Output, callback
import dash_bootstrap_components as dbc
import plotly.express as px
from Fahrmodus import *
# https://freefrontend.com/css-animated-backgrounds/page/3/
# https://alvarotrigo.com/blog/animated-backgrounds-css/


app = Dash(__name__, external_stylesheets=[dbc.themes.SLATE])

# Layout
app.layout = html.Div([  # Verwenden von html.Div, um den Hintergrund komplett abzudecken.
    # Animierter Hintergrund
    html.Div(id="stars"),  # Der Hintergrund wird hier eingefügt

    dbc.Container([  # Hier kannst du den Inhalt deiner App hinzufügen.
        html.H1("Fahrzeug Dashboard", className="text-center text-primary mb-4", style={"color": "white"}),

        dbc.Row([
            dbc.Col(dbc.Card([
                dbc.CardHeader("Durchschnittsgeschwindigkeit"),
                dbc.CardBody(html.H4(id="speed-display", className="card-title"))
            ], color="dark", inverse=True), width=3),

            dbc.Col(dbc.Card([
                dbc.CardHeader("Maximale Geschwindigkeit"),
                dbc.CardBody(html.H4(id="max-speed-display", className="card-title"))
            ], color="info", inverse=True), width=3),

            dbc.Col(dbc.Card([
                dbc.CardHeader("Minimale Geschwindigkeit"),
                dbc.CardBody(html.H4(id="min-speed-display", className="card-title"))
            ], color="info", inverse=True), width=3),
        ]),

        dbc.Row([
            dbc.Col([
                html.Label("Fahrmodus auswählen"),
                dcc.Dropdown(
                    ['fahrmodus1', 'fahrmodus2', 'fahrmodus3', 'fahrmodus4'],
                    'fahrmodus1',
                    id='fahrmodus-dropdown'
                ),
                html.Div(id='modus-output', className="mt-2")
            ], width=6),
        ]),
        dbc.Row([

            dbc.Col([
                html.Label("Abstand (Ultraschallsensor) in cm"),
                dcc.Slider(0, 60, 1, value=30, id='abstand-slider'),
                html.Div(id='abstand-output', className="mt-2")
            ], width=6),
            
            html.Button()
        ]),

        dbc.Row([
            dbc.Col(dbc.Card([
                dbc.CardHeader("Strecke total"),
                dbc.CardBody(html.H4(id="distance-display", className="card-title"))
            ], color="info", inverse=True), width=3),

            dbc.Col(dbc.Card([
                dbc.CardHeader("Fahrzeit total"),
                dbc.CardBody(html.H4(id="time-display", className="card-title"))
            ], color="info", inverse=True), width=3),
        ])
    ], fluid=True)  # Hier wird `fluid=True` verwendet, um die volle Breite zu ermöglichen.
])

# Callback
@app.callback(
    Output('modus-output', 'children'),
    Output('abstand-output', 'children'),
    Output('speed-display', 'children'),
    Output('temp-display', 'children'),
    Input('fahrmodus-dropdown', 'value'),
    Input('abstand-slider', 'value')
)
def update_dashboard(fahrmodus, abstand):
    data = get_current_values()  # Hier werden die Sensordaten abgerufen
    return (
        f'Aktueller Fahrmodus: {fahrmodus}',
        f'Eingestellter Abstand: {abstand} cm',
        f"{data['speed']} km/h",
        f"{data['temp']} °C"
    )

if __name__ == '__main__':
    app.run_server(debug=True)
