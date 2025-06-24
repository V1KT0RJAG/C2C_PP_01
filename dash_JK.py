from dash import html, Dash, dcc
import plotly.express as px
from Fahrmodus import*

app = Dash()

app.layout = html.Div(
    html.H1(id="Fahrzeug Dashboard")
    
    
    dcc.Dropdown(id="Fahrmodusauswahl", options=[Fahrmodus])
    
    
    
    
    
)




@app.callback(
    Output(),
    Input()
       
)

def graph_update():
    
    return output_values






if __name__ == '__main__'
    app.run_server(debug=True)
    
    
    
