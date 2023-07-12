import dash
from dash import html

app = dash.Dash(__name__, use_pages=True)
server=app.server

app.layout=html.Div(
        dash.page_container
    )

if __name__ == "__main__":
    app.run_server(debug=False)
