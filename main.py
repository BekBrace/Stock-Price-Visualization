# Dash Framework - stock price visualization demo
import pandas_datareader.data as web
import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import datetime

# First the layout
app = dash.Dash()
app.title = "Stock Visualization"
app.layout = html.Div(children=[
    html.H1('Stock Visualization Dashboard'),
    html.H4('Please enter the stock name'),
    dcc.Input(id="input", value='', type='text'),
    html.Div(id="output-graph")
])

# Second the interaction with the user


@app.callback(
    Output(component_id="output-graph", component_property='children'),
    [Input(component_id="input", component_property="value")]
)
def update_value(input_data):
    start = datetime.datetime(2010, 1, 1)
    end = datetime.datetime.now()
    df = web.DataReader(input_data, 'yahoo', start, end)
    return dcc.Graph(id="demo", figure={'data': [{'x': df.index, 'y': df.Close, 'type': 'line', 'name': input_data}, ], 'layout': {'title': input_data}})


if __name__ == "__main__":
    app.run_server(debug=True)
