
import pandas as pd
import numpy as np
from flask import Flask, request, jsonify
import json

app = Flask(__name__)
app.config["DEBUG"] = True # set to True while debugging

# code goes here
#@app.route('/frontEnd')
#def frontEnd():
    #return render_template('frontEndTest.html')

@app.route('/frontEnd/allocate', methods=['POST']) # link to front end
def time_allocation():
    req = request.get_data()
    dict_req = wrangle_js_data(req)
    print(dict_req)
    return '0' # doesn't matter what returns here as what we return to front end doesn't matter




# Helper Methods
def wrangle_js_data(bytes): # turns bytes of data from request.get_data() into class dict
    string = str(bytes)
    ind1 = string.find('{')
    ind2 = string.find('}')
    string = string[ind1:(ind2+1)]
    dict = json.loads(string) # turns {string} into a dict
    return dict

if __name__ == '__main__':
    app.run()
