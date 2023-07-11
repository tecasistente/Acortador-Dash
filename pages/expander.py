import dash
import pyshorteners
from dash import html, dcc, callback, Input, Output

shorter = pyshorteners.Shortener()  # Instanciar un objeto Shortener para utilizar sus métodos

dash.register_page(__name__,name="Expandir", path="/expandir")

def layout():
    layout=html.Div([
        html.H1("Expandir el Enlace", className="title"),
        
        dcc.Input(id="input-link", type="text", placeholder="Ingrese un enlace", className="input-text"),
        html.Br(),
        html.Button("Expandir", id="btn-expand", className="button"),
        html.Div(id="output-expander", className="output-container")
    ], className="container")

    return layout

@callback(
    Output("output-expander", "children"),
    Input("btn-expand", "n_clicks"),
    Input("input-link", "value"))

def expander( n_clicks, url):
    if n_clicks:
        try:
            return "Resultado: "+ shorter.tinyurl.expand(url)
        except:
            return "Resultado: "+"Introduce un enlace"
    else:
        return "Resultado: " + "Introduce un enlace"  


