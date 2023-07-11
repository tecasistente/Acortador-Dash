import dash
from dash import html, dcc, callback, Input, Output
import pyshorteners  # Importar la biblioteca pyshorteners para acortar y expandir URLs

shorter = pyshorteners.Shortener()  # Instanciar un objeto Shortener para utilizar sus métodos

dash.register_page(__name__,name="Acortador", path="/acortador")

def layout():
    layout=html.Div([
        html.H1("Acortar el Enlace", className="title"),
        
        dcc.Input(id="input-link", type="text", placeholder="Ingrese un enlace", className="input-text"),
        html.Br(),
        html.Button("Acortar", id="btn-shorten", className="button"),
        html.Div(id="output-container", className="output-container")
    ], className="container")

    return layout

@callback(
    Output("output-container", "children"),
    Input("btn-shorten", "n_clicks"),
    Input("input-link", "value"))

def short( n_clicks, url):
    if n_clicks:
        try:
            return "Resultado: "+ shorter.tinyurl.short(url)
        except:
            return "Resultado: "+"Introduce un enlace"
    else:
        return "Resultado: " + "Introduce un enlace"  
