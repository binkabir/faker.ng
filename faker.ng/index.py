import json
from flask import Flask
from flask import Response
app = Flask(__name__)

@app.route('/')
def hello_world():    

    dat = [{"firstName":"Frank", "lastName":"Joel", "email":"j.frank@gmail.com", "phone":"078399382923"}]
    resp = Response(json.dumps(dat), status=200, mimetype="application/json")
    return(resp)

if __name__ == '__main__':
    app.run()