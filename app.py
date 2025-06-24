from dash import html, dcc, Dash, Input, Output
import plotly.express as px

df = px.data.gapminder().query("year == 2007")

initial_fig = px.scatter(df, x="gdpPercap", y="lifeExp")

app = Dash(__name__)

app.layout = html.Div(
    [
    html.H1("Einführung in Dash"),
    html.Button(),
    dcc.Graph(id="my-first-graph", figure=initial_fig),
    dcc.Dropdown(id="my-first-fropdown",options=list(df["continent"].unique()), value="Asia")
    ]
)

@app.callback(
    Output("my-first-graph", "figure"),
    Input("my-first-fropdown", "value")
)
def update_first_graph(dropdown_value):
    filtered = df.query("continent == @dropdown_value")
    figure = px.scatter(filtered, x="gdpPercap", y="lifeExp")

    return figure

if __name__ == "__main__":
<<<<<<< HEAD
    app.run_server(debug=True, host= "0.0.0.0")
=======
    app.run_server(debug=True)
>>>>>>> main
