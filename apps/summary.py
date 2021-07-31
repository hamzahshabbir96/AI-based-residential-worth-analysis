# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 13:23:00 2021

@author: Hamzah
"""

import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import dash_bootstrap_components as dbc
#import utils
external_stylesheets = [dbc.themes.LUX]
import dash
import dash_table
#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
#from python-utils import Header, make_dash_table
#server = app.server
#app.config.suppress_callback_exceptions = True

#from utils import Header, make_dash_table

import pandas as pd
import pathlib

# get relative data folder
#PATH = pathlib.Path(__file__).parent
#DATA_PATH = PATH.joinpath("../data").resolve()
df=pd.read_excel('table1.xlsx')

#df_fund_facts = pd.read_csv(DATA_PATH.joinpath("df_fund_facts.csv"))
#df_price_perf = pd.read_csv(DATA_PATH.joinpath("df_price_perf.csv"))

layout=html.Div(
        
            # page 1
            
                [
                    # Row 3
                    
                            html.Div(
                                [
                                    
                                    html.H3("Summary of Forecasting"),
                                    html.Br([]),
                                    html.P(
                                        "\
                                            Forecasting comprises of two part, time series forecasting using ARIMA model  \
                                                (Autoregressive Integrated Moving Average) and Random Forest (Machine Learning algorithm). \
                                                    Forecasted results of both model is taken with weight 0.50 of each model and summed up to get final result.\
                                                        For Random Forest model, GDP per capita, Total investment and Gross national savings as input features.\
                                    ",
                                        style={"color": "#522626"},
                                        className="row",
                                    ),
                                ]
                            )
                       ,
                    # Row 4
                    html.Div(
                        [   html.Div([html.H6(".  .")]
                            ),
                            html.Div(
                                [
                                    html.H6(
                                        ["Data Table"]
                                    ),
                                    dash_table.DataTable(
                                                    id='table',
                                                    columns=[{"name": i, "id": i} for i in df.columns],
                                                    data=df.to_dict('records'),
                                                    style_cell = {
                                                            'font_family': 'cursive',
                                                            'font_size': '10px',
                                                            'text_align': 'center'
                                                        },
                                                    style_data={
                                                                'whiteSpace': 'normal',
                                                                'height': 'auto',
                                                                'lineHeight': '10px'
                                                            },
                                                    style_header={  'font_size': '10px'},
                                                    
                                                ),
                                ],
                                className="six columns",
                            ),
                            
                            html.Div(
                                [ html.Div([
                                    
                                    
                                    
                                    
                                    html.H6(
                                        "    Comparison of forecast model",
                                        className="subtitle padded",
                                    ),
                                    dcc.Graph(
                                        id="graph-1",
                                        figure={
                                            "data": [
                                                go.Bar(
                                                    x=[
                                                        "2022",
                                                        "2023",
                                                        "2024",
                                                        "2025",
                                                        "2026",
                                                    ],
                                                    y=[
                                                        "10200",
                                                        "11060",
                                                        "12050",
                                                        "12460",
                                                        "13250"

                                                    ],
                                                    marker={
                                                        "color": "#97151c",
                                                        "line": {
                                                            "color": "rgb(255, 255, 255)",
                                                            "width": 2,
                                                        },
                                                    },
                                                    name="Random Forest",
                                                ),
                                                go.Bar(
                                                    x=[
                                                        "2022",
                                                        "2023",
                                                        "2024",
                                                        "2025",
                                                        "2026",
                                                    ],
                                                    y=["10145",
                                                        "11481.5",
                                                        "11108.5",
                                                        "11675",
                                                       "12285"

                                                    ],
                                                    marker={
                                                        "color": "#dddddd",
                                                        "line": {
                                                            "color": "rgb(255, 255, 255)",
                                                            "width": 2,
                                                        },
                                                    },
                                                    name="Time Series",
                                                ),
                                            ],
                                            "layout": go.Layout(
                                                autosize=False,
                                                bargap=0.35,
                                                font={"family": "Raleway", "size": 10},
                                                height=200,
                                                
                                                hovermode="closest",
                                                legend={
                                                    "x": -0.0228945952895,
                                                    "y": -0.189563896463,
                                                    "orientation": "h",
                                                    "yanchor": "top",
                                                },
                                                margin={
                                                    "r": 0,
                                                    "t": 30,
                                                    "b": 0,
                                                    "l": 60,
                                                },
                                                showlegend=True,
                                                title="Forecast comparison",
                                                width=630,
                                                xaxis={
                                                    "autorange": True,
                                                    "range": [-0.5, 4.5],
                                                    "showline": True,
                                                    "title": "",
                                                    "type": "category",
                                                },
                                                yaxis={
                                                    "autorange": True,
                                                    "range": [0, 22.9789473684],
                                                    "showgrid": True,
                                                    "showline": True,
                                                    "title": "",
                                                    "type": "linear",
                                                    "zeroline": False,
                                                },
                                            ),
                                        },
                                        config={"displayModeBar": False},
                                    ),
                                ],
                                className="six columns",
                            ),
                        ],
                        className="row",
                        style={"margin-bottom": "35px"},
                        
                        )]
                    ),
                    # Row 5
                    html.Div(
                        [   html.Div(html.H6(".     .")),
                            html.Div(
                                [
                                    html.H6(
                                        " Trend in Price rise",
                                        className="subtitle padded",
                                    ),
                                    dcc.Graph(
                                        id="graph-2",
                                        figure={
                                            "data": [
                                                go.Scatter(
                                                    x=[
                                                        "2009",
                                                        "2010",
                                                        "2011",
                                                        "2012",
                                                        "2013",
                                                        "2014",
                                                        "2015",
                                                        "2016",
                                                        "2017",
                                                        "2018",
                                                        "2019",
                                                        "2020",
                                                        "2021",
                                                        "2022",
                                                        "2023",
                                                        "2024",
                                                        "2025",
                                                        "2026"
                                                    ],
                                                    y=[
                                                        "4802",
                                                        "5397",
                                                        "7225",
                                                        "9350",
                                                        "11007",
                                                        "10370",
                                                        "9307",
                                                        "9350",
                                                        "8585",
                                                        "9180",
                                                        "8882",
                                                        "9222",
                                                        "9052",
                                                        "10145",
                                                        "11481.5",
                                                        "11108.5",
                                                        "11675",
                                                        "12285"

                                                    ],
                                                    line={"color": "#97151c"},
                                                    mode="lines",
                                                    name="Price ₹ per sq.ft",
                                                )
                                            ],
                                            "layout": go.Layout(
                                                autosize=True,
                                                title="",
                                                font={"family": "Raleway", "size": 10},
                                                height=400,
                                                width=1040,
                                                hovermode="closest",
                                                legend={
                                                    "x": -0.0277108433735,
                                                    "y": -0.142606516291,
                                                    "orientation": "h",
                                                },
                                                margin={
                                                    "r": 20,
                                                    "t": 20,
                                                    "b": 20,
                                                    "l": 50,
                                                },
                                                showlegend=True,
                                                xaxis={
                                                    "autorange": True,
                                                    "linecolor": "rgb(0, 0, 0)",
                                                    "linewidth": 1,
                                                    "range": [2008, 2018],
                                                    "showgrid": False,
                                                    "showline": True,
                                                    "title": "",
                                                    "type": "linear",
                                                },
                                                yaxis={
                                                    "autorange": False,
                                                    "gridcolor": "rgba(127, 127, 127, 0.2)",
                                                    "mirror": False,
                                                    "nticks": 4,
                                                    "range": [0, 30000],
                                                    "showgrid": True,
                                                    "showline": True,
                                                    "ticklen": 10,
                                                    "ticks": "outside",
                                                    "title": "Rupees (₹)",
                                                    "type": "linear",
                                                    "zeroline": False,
                                                    "zerolinewidth": 4,
                                                },
                                            ),
                                        },
                                        config={"displayModeBar": False},
                                    ),
                                ],
                                className="six columns",
                            ),
                            
                            
                        ],
                        className="row ",
                    ),
                
            
        ],
       
    )

        
#if __name__ == '__main__':
    #app.run_server(debug=False)