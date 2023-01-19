import dash
from dash import Dash, dcc, html, Input, Output, dash_table, callback, ctx
import dash_bootstrap_components as dbc
import os

CSS = [dbc.themes.SLATE]

app = Dash(__name__, use_pages=True, external_stylesheets=CSS)

def createlayout():

    app_layout = html.Div([html.H1('Hackathon'), 
                        html.Div([
                            html.Div([
                                    html.Div(
                                        html.Ul( 
                                            html.H2(
                                                html.Li(
                                                    dcc.Link(
                                                        f"{page['name']}", href=page["relative_path"]
                                                    ))
                                        )),
                                    )
                                    for page in dash.page_registry.values()
                                ],style={'width': '50%', 'display': 'inline-block'}),
                        ]),
                        html.Div(children=[html.Div(dash.page_container)],id="pages_container"),dcc.Location(id="url",refresh=True),
                        
                    ],id = "div_global")
    return app_layout

app.layout = createlayout()

if __name__ == '__main__':
	app.run_server(debug=True)