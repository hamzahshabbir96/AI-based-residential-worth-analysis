import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sub
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State
#import aerosandbox as asb
#import casadi as cas
#from airplane import make_airplane
import numpy as np
import pandas as pd

#app = dash.Dash(external_stylesheets=[dbc.themes.MINTY])
#app.title = "AI based residential pricing"
#server = app.server
'''
dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                        dbc.Col(html.Img(src="/assets/logo12.png", height="46px")),
                        dbc.Col(dbc.NavbarBrand("Global database visualization", className="ml-2")),
                    ],
                    align="center",
                    no_gutters=True,
                ),
                href="/home",
            ),
            dbc.NavbarToggler(id="navbar-toggler2"),
            dbc.Collapse(
                dbc.Nav(
                    # right align dropdown menu with ml-auto className
                    [dropdown], className="ml-auto", navbar=True
                ),
                id="navbar-collapse2",
                navbar=True,
            ),
        ]
    ),
    color="dark",
    dark=True,
    className="mb-4",
)
'''

layout = dbc.Container(
    [
        dbc.Row(
            [
                dbc.Col(
                    [
                       
                        html.H5("AI Developer Alliance"),
                        html.H6("Hamzah Shabbir"),
                        html.H6("Ankita Chaturvedi"),
                    ],

                    width=True,
                ),

            ],
            align="end",
        ),
        html.Hr(),
        dbc.Row(
            [
                dbc.Col(
                    [   html.H5("Impact Factor 1"),
                        html.Div(
                            [
                            dcc.Checklist(
                                                                options=[
                                                                    {'label': 'Include IF 1 in model', 'value': 'Area'},
                                                                    
                                                                ],
                                                                value='Area'
                                                            ) ,                           
                            
                                html.P("Number of Rooms:"),
                                dcc.Slider(
                                    id="n_booms",
                                    min=1,
                                    max=7,
                                    step=1,
                                    value=3,
                                    marks={1: "1", 2: "2", 3: "3",4:"4",5:"5",6:"6",7:"7"},
                                )
                                  ,
                                html.P("Age of House[years]:"),
                                dcc.Input(id="a1", value='', type="number"),
                                html.P("Number of floors:"),
                                dcc.Slider(
                                    id="n_booms45",
                                    min=1,
                                    max=4,
                                    step=1,
                                    value=3,
                                    marks={1: "1", 2: "2", 3: "3",4:"4"},
                                ),
                                html.P("Gardens(Area):"),
                                dcc.Input(id="a3", value='', type="number"),
                                html.P("Garages(Area):"),
                                dcc.Input(id="a3rgw", value='', type="number"),
                                html.P("Number of Bathrooms:"),
                                dcc.Slider(
                                    id="n_booms5",
                                    min=1,
                                    max=5,
                                    step=1,
                                    value=3,
                                    marks={1: "1", 2: "2", 3: "3",4:"4",5:"5"},
                                ),

                                html.P("Number of Kitchens:"),
                                dcc.Slider(
                                    id="n_booms77",
                                    min=1,
                                    max=4,
                                    step=1,
                                    value=3,
                                    marks={1: "1", 2: "2", 3: "3",4:"4"},
                                ),
                                html.P("Number of Bedrooms:"),
                                dcc.Slider(
                                    id="n_booms88",
                                    min=1,
                                    max=7,
                                    step=1,
                                    value=3,
                                    marks={1: "1", 2: "2", 3: "3",4:"4",5:"5",6:"6",7:"7"},
                                ),
                            ]
                        ),
                        html.Hr(),
                        html.Div(
                            [
                                html.H5("Commands"),
                                dbc.Button(
                                    "Show Estimated Price",
                                    id="display_geometry",
                                    color="primary",
                                    style={"margin": "5px"},
                                    n_clicks_timestamp="0",
                                ),
                                dbc.Button(
                                    "Show Trend Forecast",
                                    id="run_ll_analysis",
                                    color="secondary",
                                    style={"margin": "5px"},
                                    n_clicks_timestamp="0",
                                ),
                                dbc.Button(
                                    "Analysis",
                                    id="run_vlm_analysis",
                                    color="secondary",
                                    style={"margin": "5px"},
                                    n_clicks_timestamp="0",
                                ),
                            ]
                        ),
                        html.Hr(),

                    ],
                    width=3,
                ),
               
                
                
                
                
            dbc.Col(
                    [
                        html.Div(
                            [   html.H5("Impact Factor 2"),
                                dcc.Checklist(
                                    options=[
                                        {'label': 'Include IF 2 in model', 'value': 'Area'},
                                        
                                    ],
                                    value=['Area']
                                ),
                                html.P("Distance of airport:"),
                                dcc.Input(id="b12", value='', type="number"),
                                html.P("International airport:"),
                                dcc.RadioItems(
                                            options=[
                                                {'label': 'Yes', 'value': 'Yes'},
                                                {'label': 'No', 'value': 'No'},
                                              
                                            ],
                                            value='No'
                                        ),
                                html.P("Nearest bus stop(km):"),
                                dcc.Input(id="b184", value='', type="number"),
                                html.P("Nearest Train station(km):"),
                                dcc.Input(id="b143", value='', type="number"),

                                html.P("Nearest hospital(km):"),
                                dcc.Input(id="b3t", value='', type="number"),
                                html.P("Population Density:"),
                                dcc.Input(id="b3tr", value='', type="number"),
                                html.P("Availability of public/Private transport:"),
                                dcc.Checklist(
                                    options=[
                                        {'label': 'Metro', 'value': 'Area'},
                                        {'label': 'Bus', 'value': 'Area1'},
                                        {'label': 'Tram', 'value': 'Area3'},
                                        {'label': 'Taxi', 'value': 'Area2'},
                                        {'label': 'Shared', 'value': 'Area7'},
                                        
                                    ],
                                    value=['Area']
                                ),
                                html.P("Nearest shopping mall:"),
                                dcc.Input(id="b3trr", value='', type="number"),
                              
                                
                            ]
                        ),
                        html.Hr(),
                        
                        
                    ],
                    width=3,
                ),
                
                
                
                
                
                dbc.Col(
                    [
                        html.Div(
                            [   html.H5("Impact Factor 3"),
                                dcc.Checklist(
                                    options=[
                                        {'label': 'Include IF 3 in model', 'value': 'Area'},
                                        
                                    ],
                                    value='Area'
                                ),
                                html.P("Air quality Index:"),
                                dcc.Input(id="b152", value='', type="number"),
                                
                                html.P("Ranking on cleanliness:"),
                                dcc.Input(id="b1r84", value='', type="number"),
                                html.P("Ranking on Greenery:"),
                                dcc.Input(id="b1ew43", value='', type="number"),

                                html.P("Share of Renewable Energy(%):"),
                                dcc.Input(id="b3srwt", value='', type="number"),
                                html.P("Access to electricity(% population):"),
                                dcc.Input(id="b3trfr", value='', type="number"),
                                
                              
                                
                            ]
                        ),
                        html.Hr(),
                        
                        
                    ],
                    width=3,
                ),
                
                
                
                
                
                dbc.Col(
                    [
                        html.Div(
                            [html.H5("Impact Factor 4"),
                             dcc.Checklist(
                                 options=[
                                     {'label': 'Include IF 4 in model', 'value': 'Area'},

                                 ],
                                 value='Area'
                             ),
                             html.P("No. of houses within 100m:"),
                             dcc.Input(id="b152", value='', type="number"),

                             html.P("Urban/Rural/Semi-Urban:"),
                             dcc.RadioItems(
                                 options=[
                                     {'label': 'Urban', 'value': 'Urban'},
                                     {'label': 'Rural', 'value': 'Rural'},
                                     {'label': 'Semi-Urban', 'value': 'Rural'},


                                 ],
                                 value='Urban'
                             ),
                             html.P("Waste disposal system (Y/N):"),
                             dcc.RadioItems(
                                 options=[
                                     {'label': 'Yes', 'value': 'Yes'},
                                     {'label': 'No', 'value': 'No'},


                                 ],
                                 value='Yes'
                             ),

                             html.P("Share of Renewable Energy(%):"),
                             dcc.Input(id="b3srwt", value='', type="number"),
                             html.P("Access to electricity(% population):"),
                             dcc.Input(id="b3trfr", value='', type="number"),

                             ]
                        ),
                        html.Hr(),
                    ],
                    width=3,
                )
            ]
        ),
        html.Hr(),

    ],
    fluid=True,
)
'''

def make_table(dataframe):
    return dbc.Table.from_dataframe(
        dataframe, bordered=True, hover=True, responsive=True, striped=True, style={}
    )
'''
'''
@app.callback(
    [Output("display", "figure"), Output("output", "children")],
    [
        Input("display_geometry", "n_clicks_timestamp"),
        Input("run_ll_analysis", "n_clicks_timestamp"),
        Input("run_vlm_analysis", "n_clicks_timestamp"),
    ],
    [State("n_booms", "value"), State("wing_span", "value"), State("alpha", "value"),],
)
def display_geometry(
    display_geometry, run_ll_analysis, run_vlm_analysis, n_booms, wing_span, alpha,
):
    ### Figure out which button was clicked
    try:
        button_pressed = np.argmax(
            np.array(
                [
                    float(display_geometry),
                    float(run_ll_analysis),
                    float(run_vlm_analysis),
                ]
            )
        )
        assert button_pressed is not None
    except:
        button_pressed = 0

    ### Make the airplane
    airplane = make_airplane(n_booms=n_booms, wing_span=wing_span,)
    op_point = asb.OperatingPoint(density=0.10, velocity=20, alpha=alpha,)
    if button_pressed == 0:
        # Display the geometry
        figure = airplane.draw(show=False, colorbar_title=None)
        output = "Please run an analysis to display the data."
    elif button_pressed == 1:
        # Run an analysis
        opti = cas.Opti()  # Initialize an analysis/optimization environment
        ap = asb.Casll1(
            airplane=airplane, op_point=op_point, opti=opti, run_setup=False
        )
        ap.setup(verbose=False)
        # Solver options
        p_opts = {}
        s_opts = {}
        # s_opts["mu_strategy"] = "adaptive"
        opti.solver("ipopt", p_opts, s_opts)
        # Solve
        try:
            sol = opti.solve()
        except RuntimeError:
            sol = opti.debug
            raise Exception("An error occurred!")

        figure = ap.draw(show=False)  # Generates figure

        output = make_table(
            pd.DataFrame(
                {
                    "Figure": ["CL", "CD", "CDi", "CDp", "L/D"],
                    "Value": [
                        sol.value(ap.CL),
                        sol.value(ap.CD),
                        sol.value(ap.CDi),
                        sol.value(ap.CDp),
                        sol.value(ap.CL / ap.CD),
                    ],
                }
            )
        )

    elif button_pressed == 2:
        # Run an analysis
        opti = cas.Opti()  # Initialize an analysis/optimization environment
        ap = asb.Casvlm1(
            airplane=airplane, op_point=op_point, opti=opti, run_setup=False
        )
        ap.setup(verbose=False)
        # Solver options
        p_opts = {}
        s_opts = {}
        # s_opts["mu_strategy"] = "adaptive"
        opti.solver("ipopt", p_opts, s_opts)
        # Solve
        try:
            sol = opti.solve()
        except RuntimeError:
            sol = opti.debug
            raise Exception("An error occurred!")

        figure = ap.draw(show=False)  # Generates figure

        output = make_table(
            pd.DataFrame(
                {
                    "Figure": ["CL", "CDi", "L/Di"],
                    "Value": [
                        sol.value(ap.CL),
                        sol.value(ap.CDi),
                        sol.value(ap.CL / ap.CDi),
                    ],
                }
            )
        )

    figure.update_layout(
        autosize=True,
        # width=1000,
        # height=700,
        margin=dict(l=0, r=0, b=0, t=0,),
    )

    return (figure, output)
'''

#try:  # wrapping this, since a forum post said it may be deprecated at some point.
 #   app.title = "Aircraft Design with Dash"
#except:
 #   print("Could not set the page title!")


#if __name__ == "__main__":
 #   app.run_server(debug=False)
