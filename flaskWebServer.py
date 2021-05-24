import protoBuffClient
from protoBuffClient import json_string
import flask
from flask import jsonify,render_template, make_response
import json

app = flask.Flask(__name__,template_folder='C:/Users/raja.omer.AFINITI/AppData/Local/Programs/Python/Python39/templates')
app.config["DEBUG"] = True

@app.route('/getUsageData', methods=['GET'])
def home():
    resp = render_template('Test.html', data=json_string)
    return resp

app.run()
