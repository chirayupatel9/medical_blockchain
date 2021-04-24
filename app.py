import json

import requests
from flask import Flask, jsonify
from flask import render_template, request
from flask_cors import CORS

from dbconnect import add_patient_to_db, add_doctor_to_db, fetch_all_patient
from dbconnect import fetch_patient, assigned_doc_to_pat
from mongo import User

app = Flask(__name__)
app.config['CORS_HEADERS'] = 'Content-Type'
app.secret_key = "hello"

# The node with which our application interacts, there can be multiple
# such nodes as well.
CONNECTED_NODE_ADDRESS = "http://127.0.0.1:8000"

posts = []

CORS(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/printchain')
def printchain():
    get_chain_address = "{}/chain".format(CONNECTED_NODE_ADDRESS)
    response = requests.get(get_chain_address)
    chain = json.loads(response.content)
    return jsonify(chain)


@app.errorhandler(404)
def not_found(error=None):
    response = {'status': 400,
                "message": "Not Found" + request.url
                }
    return jsonify(response)


@app.route('/add_patient', methods=['POST'])
def add_patient():
    if request.method == 'POST':
        request_json = request.get_json()

        new_tx_address = "{}/new_transaction".format(CONNECTED_NODE_ADDRESS)
        add_patient_to_db(request_json)
        request_json["_id"] = str(request_json['_id'])

        requests.post(new_tx_address,
                      json=request_json,
                      headers={'Content-type': 'application/json'})
        return request_json
    else:
        return not_found()


@app.route('/add_doctor', methods=['POST'])
def add_doctor():
    if request.method == "POST":
        request_json = request.get_json()

        new_tx_address = "{}/new_transaction".format(CONNECTED_NODE_ADDRESS)

        add_doctor_to_db(request_json)
        request_json["_id"] = str(request_json['_id'])
        requests.post(new_tx_address,
                      json=request_json,
                      headers={'Content-type': 'application/json'})
        return request_json
    else:
        return not_found()


@app.route('/view_patients')
def view_patients():
    return fetch_all_patient()


@app.route('/view_patients/<pname>')
def afteradding(pname):
    return fetch_patient(pname)


@app.route('/update', methods=['PUT'])
def updating_doc():
    _json = request.json
    pat = _json['patientname']
    docname = _json['doctorname']
    docnotes = _json['doctor_notes']
    # print(pat,docnotes,docname)
    if pat and docname and docnotes and request.method == "PUT":
        new_tx_address = "{}/new_transaction".format(CONNECTED_NODE_ADDRESS)

        assigned_doc_to_pat(_json)
        response = {'status': 200,
                    "message": "Updated patient with doctor " + request.url + _json
                    }
        requests.post(new_tx_address,
                      json=_json,
                      headers={'Content-type': 'application/json'})
        return response
    else:
        return not_found()


@app.route('/user/signup', methods=['POST', 'GET'])
def signup():
    return User().signup()


@app.route('/user/signout')
def signout():
    return User().signout()


@app.route('/user/login', methods=['POST'])
def login():
    return User().login()


@app.route('/user/profile', methods=['POST', 'GET'])
def profile():
    return User().profile()
