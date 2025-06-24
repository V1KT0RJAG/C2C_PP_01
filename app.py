from dash import html, dcc, Dash, Input, Output
import plotly.express as px

# Daten vorbereiten
df = px.data.gapminder().query("year == 2007")
initial_fig = px.scatter(df, x="gdpPercap", y="lifeExp")

# App initialisieren
app = Dash(__name__)

# App-Layout definieren
app.layout = html.Div(
    [
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

# Server starten
if __name__ == "__main__":
    app.run_server(debug=True, host= "0.0.0.0")
