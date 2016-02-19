import os
import json
from db import DB
from flask import Flask
from flask import Response
app = Flask(__name__)
PRODUCTION = False
if PRODUCTION:
    PROJECT_PATH = os.path.split(os.path.abspath((__file__)))[0] +  os.path.sep
else:
    PROJECT_PATH = os.path.dirname(os.path.split(os.path.abspath((__file__)))[0]) +  os.path.sep

@app.route('/api/v1/faker/people')
def get_fake_people():

    dat = DB().find_people()
    resp = Response(json.dumps(dat), status=200, mimetype="application/json")
    return resp

@app.route('/api/v1/faker/people/<int:numOfPeople>')
def get_number_of_people(numOfPeople):

    dat = DB().find_people()[:numOfPeople]
    resp = Response(json.dumps(dat), status=200, mimetype="application/json")
    return resp

@app.route('/api/v1/faker/emails')
def get_emails():

    data = DB().find_emails()
    resp = Response(json.dumps(data), status=200, mimetype="application/json")
    return resp

@app.route('/api/v1/faker/emails/<int:numOfEmails>')
def get_num_of_emails(numOfEmails):

    data = DB().find_emails()[:numOfEmails]
    resp = Response(json.dumps(data), status=200, mimetype="application/json")
    return resp

if __name__ == '__main__':
    app.run(host='0.0.0.0')
