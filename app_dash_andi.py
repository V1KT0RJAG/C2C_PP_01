from dash import html, dcc, Dash, Input, Output, State  
import plotly.express as px
import dash_bootstrap_components as dbc 

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

df = px.data.gapminder().query("year == 2007")
initial_fig = px.scatter(df, x="gdpPercap", y="lifeExp")

app.layout = html.Div([
    dbc.Row(
        [
        html.H1("Einführung in Dash"), 
        html.H2("Unterüberschrift"), 
        dcc.Graph(id = "my-first-graph", figure = initial_fig), 
        ]
        ),
    dbc.Row(
        [
        dbc.Col([
            dcc.Dropdown(id="Fahrmodi", options=list(df["continent"].unique()), value="Asia")
            ]),
        dbc.Col([
            dcc.Dropdown(id="Land", options=list(df["country"].unique()))

            ]),
        html.P(id="description")
        ]
        )
    ])

@app.callback(
    Output("my-first-graph", "figure", allow_duplicate=True), Output("description", "children", allow_duplicate=True),
    Input("Fahrmodi", "value"),
    prevent_initial_call=True,
    allow_duplicate=True
)
def update_first_graph(continent):
    filtered = df.query("continent == @continent")
    figure = px.scatter(filtered, x="gdpPercap", y="lifeExp")
    
    description = f"Du hast hier das BIP und die Lebenserwartung für {continent}"
    
    return figure, description

@app.callback(
    Output("Land", "options"), 
    Input("Fahrmodi", "value"),
    allow_duplicate=True
)
def define_options(continent):
    return list(df.query("continent == @continent")["country"].unique())

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8050)
