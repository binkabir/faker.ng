import os
import json
from db import DB
from flask import Flask , render_template, url_for, redirect,request,jsonify
from flask import Response

app = Flask(__name__)
app.config.from_pyfile("application.cfg") #added the configuration params file
PRODUCTION = False
if PRODUCTION:
    PROJECT_PATH = os.path.split(os.path.abspath((__file__)))[0] +  os.path.sep
else:
    PROJECT_PATH = os.path.dirname(os.path.split(os.path.abspath((__file__)))[0]) +  os.path.sep

@app.route('/',methods=['GET'])
def home():
    return render_template('index.html')
    
# @app.route('/api/v1/faker/people')
#def get_fake_people():

#    dat = DB().find_people(None)
#    resp = Response(json.dumps(dat), status=200, mimetype="application/json")
#    return resp


@app.route('/api/v1/faker/people/')
@app.route('/api/v1/faker/people/<int:numOfPeople>')
def get_number_of_people(numOfPeople = app.config["DEFAULT_QUERY_SIZE"]):
 
    dat = DB().find_people()[:numOfPeople]
    resp = Response(json.dumps(dat), status=200, mimetype="application/json")
    return jsonify(size=len(dat), response = dat)

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
    app.run(host='0.0.0.0', debug=True)
