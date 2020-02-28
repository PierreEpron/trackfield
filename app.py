# -*- coding: utf-8 -*-
import dash, os, json
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
from pathlib import Path
import pandas as pd
import numpy as np

data = {}

'''
    Gender : path.parts[2]
    Sport : path.parts[3]
    Year : path.name
'''


''' DASH (2 en 1) '''

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Trackfield Data Viz'),
    dcc.Graph(
        id='year_graph',
        figure={
            'data': [
                go.Scatter(
                    x=[1, 2, 3], 
                    y=[4, 1, 2]
                )
        ],
            'layout': {
                'title': 'Dash Data Visualization'
        }
    }
)
])

if __name__ == '__main__':
    app.run_server(debug=True)