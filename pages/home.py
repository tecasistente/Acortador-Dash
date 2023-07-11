import dash
from dash import html

dash.register_page(__name__,name="Enlaces", path="/")


def layout():
    layout = html.Div([
        html.H1("Acortador de Enlaces", className="title"),
        html.A(
            html.Button("Acortar", className="button"),
            href="/acortador"
        ),
        html.A(
            html.Button("Expandir", className="button"),
            href="/expandir"
        )
    ], className="container")

    return layout

