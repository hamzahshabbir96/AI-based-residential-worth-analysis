import dash_html_components as html
import dash_bootstrap_components as dbc

# needed only if running this as a single page app
#external_stylesheets = [dbc.themes.LUX]

#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# change to app.layout if running as single page app instead
layout = html.Div([
    dbc.Container([
        dbc.Row([
            dbc.Col(html.H1("ABOUT THIS PROJECT", className="text-center")
                    , className="mb-5 mt-5")
        ]),
        dbc.Row([
            dbc.Col(html.H5(children='This application is part of India PropTech Hackathon organised by Hacker Earth.'
                                     )
                    , className="mb-4")
            ]),

        dbc.Row([
            dbc.Col(html.H5(children='This app is based on using Neural network and machine learning to make a model '
                                     'that can be used to analyze residential market and attract middle class individual of India '
                                     'by value addition. This app shows proposed model for such approach. '
                                     'Description and approach of this project can be understood from chart below.')
                    , className="mb-5")
        ]),

        dbc.Row([
        html.Img(src="/assets/project.jpg"),
        html.Hr(),


               html.Hr(),
               html.H5("If you find any bug or abnormalities in this project, please report me on hamzahshabbir7@gmail.com"
                      ),
                      html.A("Special Thanks to “NEC Corporation India” and “Mitsubishi Corporation India” for providing this oppurtunity of working in this project",
                             href="https://www.hackerearth.com/"),

    ])

])
])
# needed only if running this as a single page app
# if __name__ == '__main__':
# app.run_server(host='127.0.0.1', debug=True)
