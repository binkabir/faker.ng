import json
from db import DB
from flask import Flask
from flask import Response
app = Flask(__name__)


@app.route('/api/v1/faker/people')
def get_fake_people():

    dat = DB().find_people()
    resp = Response(json.dumps(dat), status=200, mimetype="application/json")
    return resp

@app.route('/api/v1/faker/people/<int:numOfPeople>')
def get_no_of_people(numOfPeople):

    dat = DB().find_people()[0:numOfPeople]
    resp = Response(json.dumps(dat), status=200, mimetype="application/json")
    return resp

if __name__ == '__main__':
    app.run()
