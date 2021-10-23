
import pandas as pd
import numpy as np
from flask import Flask, request, jsonify
import json
import codecs

app = Flask(__name__)
app.config["DEBUG"] = True # set to True while debugging

# code goes here
@app.route('/json-example', methods=['POST']) # link to front end
def json_example():
    data = request.json["name"]
    return data



if __name__ == '__main__':
    app.run()
