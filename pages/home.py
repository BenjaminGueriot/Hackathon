import dash
from dash import html
import base64

dash.register_page(__name__, path='/')

layout = html.Div(children=[

    html.Div(children=[
        
        html.H1(children='yo'), 
        html.Br()
    ]),
])