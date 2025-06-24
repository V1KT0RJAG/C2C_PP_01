from dash import html, dcc, Dash, Input, Output
import plotly.express as px
import carmain

import pandas as pd
import numpy as np

# Load the CSV file
#df = pd.read_csv('simulated_car_data.csv', delimiter=',')
df 

print(df.head(10))

#df = px.data.gapminder()
fig = px.line(log_df, x="time", y="speed")
fig.show()

# app = Dash(__name__)

# app.layout = html.Div(
#     [
#     html.H1("Einführung in Dash"),
#     #html.Button(),
#     dcc.Graph(id="my-first-graph", figure=initial_fig),
#     #dcc.Dropdown(id="my-first-fropdown",options=list(df["speed"].unique()), value="Asia")
#     ]
# )

# @app.callback(
#     Output("my-first-graph", "figure"),
#     Input("my-first-fropdown", "value")
# )
# def update_first_graph(dropdown_value):
#     #filtered = df.query("speed == @dropdown_value")
#     #figure = px.scatter(filtered, x="time", y="speed")

#     return figure

# if __name__ == "__main__":
#     app.run_server(debug=True)