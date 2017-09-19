from flask import Flask, request, Response, send_from_directory, render_template
from flask_cors import CORS, cross_origin
# Jsonify lib
import json
# DB lib
from db import DB

app = Flask(__name__)
CORS(app) # Evita problemas de cross_origin


@app.route("/hello_world")
def hello_world():
    return "Hello world"


@app.route("/hello_world_json")
def hello_world_json():

    result = {"hello": "world"}
    status = 200
    
    resp = Response(json.dumps(result), status=status, mimetype='application/json')
    resp.headers['Access-Control-Allow-Origin'] = '*'

    return resp


@app.route("/hello_world/<argument>")
def hello_world_argument(argument):

    result = {"argument": argument}
    status = 200
    
    resp = Response(json.dumps(result), status=status, mimetype='application/json')
    resp.headers['Access-Control-Allow-Origin'] = '*'

    return resp


@app.route("/methods", methods = ["GET", "POST"])
def ruta():

    if request.method == "GET":
        result = 'GET request is not allowed'
        status = 501

    elif request.method == "POST":
        result = 'POST method is allowed :)'
        status = 200

    resp = Response(json.dumps(result), status=status, mimetype='application/json')
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


"""
Parte 2: API dinámica
"""
@app.route("/users", methods = ["GET", "POST"])
def users():

    if request.method == "GET":
        db = DB()
        result = db.get_all_users()
        status = 200
        db.conn.close()

    elif request.method == "POST":
        db = DB()
        data = request.get_json(force=True)
        result = db.create_user(data)
        status = 201
        db.conn.close()

    resp = Response(json.dumps(result), status=status, mimetype='application/json')
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp


@app.route("/users/<id>", methods = ["GET", "PATCH"])
def users_id(id):

    if request.method == "GET":
        db = DB()
        result = db.get_user_by_id(id)
        status = 200

    elif request.method == "PATCH":
        request.get_json(force=True)
        db.create_user()
        status = 200

    resp = Response(json.dumps(result), status=status, mimetype='application/json')
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp



if __name__ == "__main__":
    app.run(debug = True)
