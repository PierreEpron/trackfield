# -*- coding: utf-8 -*-
import dash, os, json, operator
import dash_table
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

import pandas as pd
import numpy as np

from settings import *
from models import *


tfm = TrackfieldModel('csv')
with open('probs.txt', 'w', encoding='utf-8') as f:
    f.writelines('\n'.join(';'.join(str(value) for value in row) for row in get_first_of_each(tfm, ['year', 'sport_id'], 'perf_0')))

def perf_to_secs(v):
    v = v.split('.')
    if len(v) == 1:
        return int(v[0])
    elif len(v) == 2:
        return int(v[0]) * 60 + int(v[1])
    elif len(v) == 3:
        return int(v[0]) * 60 * 60 + int(v[1]) * 60 + int(v[2])
def split_date(v):
    v = v.split(' ')
    _v = []
    for i in range(0, len(v)):
        if v[i] != '':
            _v.append(v[i])
    return _v 
def date_to_dt(v, date):
    format = '%Y %b %d'
    v = split_date(v)
    if len(v) == 1:
        return pd.to_datetime('%s %s 01'%(date, v[0]), format=format)
    elif len(v) == 2:
        return pd.to_datetime('%s %s %s'%(date, v[0], v[1]), format=format)

# print(df[operator.and_(df['sport_id'] == 'MA6', df['year'] == 1891)]['perf_0'].apply(perf_to_secs))   
# print(df[operator.and_(df['sport_id'] == 'MA6', df['year'] == 1891)]['perf_0'])  
# print(df[operator.and_(df['sport_id'] == 'MA6', df['year'] == 1891)]['date'].apply(date_to_dt, args=(1891,)))   
# print(df[operator.and_(df['sport_id'] == 'MA6', df['year'] == 1891)]['date'])  


''' DASH (2 en 1) '''

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)


# current = df[operator.and_(df['sport_id'] == 'MA6', df['year'] == 1891)]
# current['perf_0'] = current['perf_0'].apply(perf_to_secs)  
# current['date'] = current['date'].apply(date_to_dt, args=(1891,))
# current = current.sort_values(by=['date'])


app.layout = html.Div(
    style={
        'width':'30%'
    },
    children=[
        # html.H1(children='Trackfield Data Viz'),
        dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in COLS_VIEW],
            data=tfm.actif[COLS_VIEW].to_dict('records'),
            style_table={
                'height': '300px',
                'overflowY': 'scroll',
                'border': 'thin lightgrey solid',
            },
            editable=True,
            filter_action="native",
            sort_action="native",
            sort_mode="multi",
            column_selectable="multi",
            row_selectable="multi",
            row_deletable=True,
            selected_columns=[],
            selected_rows=[],
            page_action="native",
            page_current= 0,
            page_size= 100,
        ),    
        # dcc.Graph(
        #     id='year_graph',
        #     figure={
        #         'data': [
        #             dict(
        #                 x= current['date'],
        #                 y= current['perf_0'],
        #                 name = 'tralalal',
        #                 marker=dict(
        #                     color='rgb(55, 83, 109)'
        #                 )                
        #             )
        #         ],
        #         'layout': {
        #             'title': 'Dash Data Visualization'
        #         }
        #     }   
        # )
    ]
)

if __name__ == '__main__':
    app.run_server(debug=True)