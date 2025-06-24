from dash import html, Dash, dcc, Input, Output,callback
import plotly.express as px
from Fahrmodus import*

app = Dash(external_stylesheets=[dbc.themes.Slate])

app.layout = html.Div(
    html.H1(id="Fahrzeug Dashboard"),
    
    
    
    dcc.Dropdown(['fahrmodus1', 'fahrmodus2', 'fahrmodus3', 'fahrmodus4'], 'fahrmodus1', id='Fahrmodusauswahl'),
    html.Div(id='dd-output-container')

    
    dcc.Slider(id="Bitte den Abstand für den Ultraschallsensor einstellen in cm", 0, 60, 1, value=30)
    
    
    
    
    
)




@app.callback(
    Output('dd-output-container', 'children'),
    Input('demo-dropdown', 'value')
       
)

def graph_update():
    
    return output_values

def update_output(value):
    return f'You have selected {value}




if __name__ == '__main__'
    app.run_server(debug=True)
    
    
    
