import dash
import dash_labs as dl
import dash_bootstrap_components as dbc
from dash import html

import flask
from flask import Flask, render_template, request,redirect,url_for
from flask_restx import Resource, Api

server = flask.Flask(__name__)



app = dash.Dash(
    __name__, server=server, plugins=[dl.plugins.pages],external_stylesheets=[dbc.themes.CYBORG], update_title='Cargando...'
)

navbar = dbc.NavbarSimple([
    dbc.NavItem(dbc.NavLink( (html.Img(src='/assets/info.png', height="30",className="center blanco")), href="/about"),class_name="mx-3"),
    dbc.NavItem(dbc.NavLink( (html.Img(src='/assets/app.png', height="30",className="center blanco")), href="/maptrees5"),class_name="mx-3"),
    dbc.NavItem(dbc.NavLink( (html.Img(src='/assets/arbol2.png', height="35",className="center blanco")), href="/storytelling"),class_name="mx-3"),
    dbc.NavItem(dbc.NavLink( (html.Img(src='/assets/prediccion.png', height="30",className="center blanco")), href="/model"),class_name="mx-3"),
    dbc.NavItem(dbc.NavLink( (html.Img(src='/assets/equipo.png', height="30",className="center blanco")), href="/equipo"),class_name="mx-3"),
    dbc.NavItem(dbc.NavLink( (html.Img(src='/assets/mail.png', height="25",className="center blanco")), href="/mail"),class_name="mx-3")
    
    ],
    brand="Team 123",
    brand_href="/",
    color= "dask",
    dark=True,
    
)

app.layout = dbc.Container(
    [navbar, dl.plugins.page_container],
    fluid=True,
)

@server.route('/hello')
def hello():
    return 'Hello, World!'

@server.route('/estado')
def index():
    return flask.redirect('/tablas')

"""
@server.route('/model', methods=["GET", "POST"])
def model():
    username = None
    value = 0
    if request.method == 'POST':
        username = request.form.get("username", None)

    def calculate_value_based_on_username(user_given_name):
        return len(user_given_name)

    if username:
        value = calculate_value_based_on_username(username)
        print(value)
        return flask.redirect('/model')
        #return flask.redirect('/model', username=username, value=value)
    return flask.redirect('/model')
"""

@server.route('/result', methods=['POST'])
def on_post():
    data = flask.request.form
    print(data)
    return flask.redirect(flask.request.url)

api = Api(server)

@api.route("/api")
class DemoAPI(Resource):
    def get(self):
        return {"message":"This is a message from Rest"}



if __name__ == "__main__":
    app.run_server(host='127.0.0.1', port=8060, debug=True)