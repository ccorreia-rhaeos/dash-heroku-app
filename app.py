# Import required libraries
import os
from random import randint


import flask
from dash import Dash, callback, html, dcc


# Setup the app
# Make sure not to change this file name or the variable names below,
# the template is configured to execute 'server' on 'app.py'
server = flask.Flask(__name__)
server.secret_key = os.environ.get('secret_key', str(randint(0, 1000000)))
app = Dash(__name__, server=server)

def create_dash_layout(app):

    # Set browser tab title
    app.title = "Chase's Analysis App" 
    
    # Header
    header = html.Div([html.Br(), dcc.Markdown(""" # Hi. I'm your Dash app."""), html.Br()])

    # Body 
    body = html.Div([dcc.Markdown(""" ## I'm ready to serve static files on Heroku. Just look at this! """)])

    # Footer
    footer = html.Div([html.Br(), html.Br(), dcc.Markdown(""" ### Built within Python using [Dash](https://plotly.com/dash/)""")])
    
    # Assemble dash layout 
    app.layout = html.Div([header, body, footer])

    return app

# Construct the dash layout
create_dash_layout(app)
# Put your Dash code here


# Run the Dash app
if __name__ == '__main__':
    app.server.run(debug=True, threaded=True)
