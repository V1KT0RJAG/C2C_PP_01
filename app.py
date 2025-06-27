from dash import html, dcc, Dash, Input, Output
import plotly.express as px
import pandas as pd
import numpy as np

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

app = Dash(__name__)

app.layout = html.Div(
    [
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

if __name__ == "__main__":
    app.run_server(debug=True)