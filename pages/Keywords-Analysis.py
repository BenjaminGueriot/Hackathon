import dash
from dash import html, dcc, callback, Input, Output, ctx
import operator
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import json
import io
import os

#import data-------------------------------------------------------------------

buffer = io.StringIO()



dash.register_page(__name__)

layout = html.Div([
    html.H1('Analysis'),
    html.Div([
    dcc.Graph(id="graphhaut",style={'width': '100%','height':'50%', 'display': 'inline-block'})],id="fig1",),
    html.Div([
        dcc.Graph(id="graphbas",style={'width': '40%','height':'50vh', 'display': 'inline-block'}),
        dcc.Graph(id="graphbas2",style={'width': '60%','height':'50vh', 'display': 'inline-block'})
    ],id="fig2"),
],id="div_global")


@callback(
    Output("graphhaut", "figure"),
    Input("graphhaut", "clickData"),
    Input("dropdown", "value"))
def update_bar_chart(clickData, year):

    if clickData is None:
        clickData = None
        global data
        data = open_data()
        fig = createBarChart(year, None)
        return fig
    else:
        index = clickData["points"][0]["pointNumber"]
        fig = createBarChart(year, index)
        return fig

def createBarChart(year, index):

    day = []
    values = []
    lcolor=[]
    data_day = data["metadata-all"]["fr"]["day"][year]

    data_month_sorted = sorted(data_day.keys(),key=int)
    for i in data_month_sorted:
        data_day_sorted = sorted(data_day[str(i)],key=int)

        for keys in data_day_sorted:
            day_str = str(keys) + "/" + str(i) + "/" + str(year)
            day.append(day_str)
            values.append(data_day[str(i)][keys]["num"])
            if len(lcolor) == index:
                lcolor.append('rgba(222,45,38,0.8)')
            else:
                lcolor.append('rgba(149,177,209,1)')


    df = pd.DataFrame(values,index=day,columns=["nb_articles"])

    fig = go.Figure(data=[go.Bar(x= df.index.values, y=df['nb_articles'], marker=dict(color = lcolor))])
    fig.update_layout(title_text='Number of articles per day',title_x=0.5, font=dict(family="Courier New, Monospace"))

    return fig