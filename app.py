from dash import html, dcc, Dash, Input, Output
import plotly.express as px
import pandas as pd
import numpy as np

<<<<<<< HEAD
# Load the CSV file
df = pd.read_csv('sonic_log_good_data.csv', delimiter=',')

print(type(df))
print(df.head(5))

print(df["speed"].min())
print(df["speed"].max())
print(df["speed"].mean())

print(df["timestamp"].max()-df["timestamp"].min())

initial_fig = px.line(df, x="timestamp", y="speed")

#initial_fig.show()  -> Nur zum test Zwecke, nicht aktivieren
=======
# Daten vorbereiten
df = px.data.gapminder().query("year == 2007")
initial_fig = px.scatter(df, x="gdpPercap", y="lifeExp")
>>>>>>> 675e620cf6fa3777bd37c05e7d597a69eeead118

# App initialisieren
app = Dash(__name__)

# App-Layout definieren
app.layout = html.Div(
    [
<<<<<<< HEAD
    html.H1("Log of PiCar Gruppe2"),
    dcc.Graph(id="my-first-graph", figure=initial_fig),
    #dcc.Dropdown(id="my-first-fropdown",options=list(df["continent"].unique()), value="Asia")
    ]
)

# @app.callback(
#     Output("my-first-graph", "figure"),
#     Input("my-first-fropdown", "value")
# )
# def update_first_graph(dropdown_value):
#     filtered = df.query("continent == @dropdown_value")
#     figure = px.scatter(filtered, x="gdpPercap", y="lifeExp")

#     return figure
=======
        html.H1("Einführung in Dash"),
        html.Button("Klick mich", id="dummy-button"),  # Optional, da ungenutzt
        dcc.Graph(id="my-first-graph", figure=initial_fig),
        dcc.Dropdown(
            id="my-first-dropdown",
            options=[{"label": continent, "value": continent} for continent in df["continent"].unique()],
            value="Asia"
        )
    ]
)

# Callback zur Aktualisierung der Grafik
@app.callback(
    Output("my-first-graph", "figure"),
    Input("my-first-dropdown", "value")
)
def update_first_graph(dropdown_value):
    filtered = df.query("continent == @dropdown_value")
    figure = px.scatter(filtered, x="gdpPercap", y="lifeExp")
    return figure
>>>>>>> 675e620cf6fa3777bd37c05e7d597a69eeead118

# Server starten
if __name__ == "__main__":
    app.run_server(debug=True, host= "0.0.0.0")
