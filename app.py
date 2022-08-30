import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State

import plotly.graph_objs as go
import pandas as pd

########### Define your variables ######

tabtitle = 'Analysis of Streaming Platforms'
sourceurl = ''
githublink = 'https://github.com/purnimavenkatram/exploratory-data-analysis'
# here's the list of possible columns to choose from.

df = pd.read_csv('assets/tv_shows.csv',encoding='utf-8')
list_of_columns =['Shows by year','Shows by age group','Shows by rating', 'Top 5 shows']
list_of_variables=['Year','Age','IMDb','Custom']
########### Initiate the app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
server = app.server
app.title=tabtitle

########### Set up the layout

app.layout = html.Div(children=[
    html.H1('TV shows on different streaming platforms'),
    html.Div([
        html.Div([
                html.H6('Select a variable for analysis:'),
                dcc.Dropdown(
                    id='options-drop',
                    options=[{'label': i, 'value': i} for i in list_of_columns],
                    value='Shows by year'
                ),
        ], className='two columns'),
        html.Div([dcc.Graph(id='figure-1'),
            ], className='ten columns'),
    ], className='twelve columns'),
    html.A('Code on Github', href=githublink),
    html.Br(),
    html.A("Data Source", href=sourceurl),
    ]
)


# make a function that can intake any varname and produce a map.
@app.callback(Output('figure-1', 'figure'),
             [Input('options-drop', 'value')])
def make_figure(varname):
    mygraphtitle = f' {varname}'
    mycolorscale = 'ylorrd' # Note: The error message will list possible color scales.
    mycolorbartitle = "Count"
    if varname == "Top 5 Shows":         
       df_slice=df[ list_of_variables[list_of_columns.index(varname)]].value_counts()
       df_slice_v2=pd.Dataframe({list_of_variables[list_of_columns.index(varname)]: df_slice.index,'Count':df_slice.values})
       fig = px.histogram(df_slice_v2,x=list_of_variables[list_of_columns.index(varname)],y='Count',barmode='group',height=400)
       return fig
    else:
       df_slice=df[ list_of_variables[list_of_columns.index(varname)]].value_counts()
       df_slice_v2=pd.Dataframe({list_of_variables[list_of_columns.index(varname)]: df_slice.index,'Count':df_slice.values})
       fig = px.histogram(df_slice_v2,x=list_of_variables[list_of_columns.index(varname)],y='Count',barmode='group',height=400)
       return fig
    

############ Deploy
if __name__ == '__main__':
    app.run_server(debug=True)
