
import pandas as pd
import numpy as np
from flask import Flask, request, jsonify
import json
import codecs

app = Flask(__name__)
app.config["DEBUG"] = True # set to True while debugging
facts = 10

# code goes here
@app.route('/time-allocation', methods=['POST']) # link to front end
def time_allocation():
    data = request.json["name"]
    a = [request.json["name"], request.json["age"]]
    print(a)
    print(facts)
    return data # doesn't matter what returns here as what we return to front end doesn't matter




# Helper Methods



if __name__ == '__main__':
    app.run()
