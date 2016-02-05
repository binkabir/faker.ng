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

if __name__ == '__main__':
    app.run()
