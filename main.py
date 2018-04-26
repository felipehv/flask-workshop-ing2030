from flask import Flask, request, Response
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




@app.route("/hello_json")
def hello_world_json():

    result = {"hello": "world"}
    status = 200
    
    resp = Response(json.dumps(result), status=status, mimetype='application/json')

    return resp

@app.route("/hello_world/<argument>")
def hello_world_argument(argument):

    result = {"argument": argument}
    status = 200
    
    resp = Response(json.dumps(result), status=status, mimetype='application/json')

    return resp







@app.route("/methods", methods = ["GET", "POST"])
def ruta():

    if request.method == "GET":
        result = 'GET request is not allowed'
        status = 501

    elif request.method == "POST":
        result = 'POST method is allowed :)'
        status = 201

    resp = Response(json.dumps(result), status=status, mimetype='application/json')
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
        data = request.get_json()
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
        db = DB()
        data = request.get_json(force=True)
        db.modify_user(id, data)
        result = 'Ok'
        status = 200


    resp = Response(json.dumps(result), status=status, mimetype='application/json')
    resp.headers['Access-Control-Allow-Origin'] = '*'
    return resp

@app.route('/users/<id>/phones', methods=['GET', 'POST'])
def user_phones(id):
    
    if request.method == 'GET':
        db = DB()
        result = db.get_phones_by_user_id(id)
        status = 200
        db.conn.close()

    elif request.method == "POST":
        db = DB()
        data = request.get_json()
        result = db.create_phone(id, data)
        db.conn.close()
        status = 201


    resp = Response(json.dumps(result), status=status, mimetype='application/json')
    return resp

if __name__ == "__main__":
    app.run(debug = True, host='0.0.0.0')
    # 127.0.0.1
