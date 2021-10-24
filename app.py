
import pandas as pd
import numpy as np
from flask import Flask, request, jsonify
import json

app = Flask(__name__)
app.config["DEBUG"] = True # set to True while debugging

# code goes here

@app.route('/frontEnd/allocate', methods=['POST']) # link to front end
def time_allocation():
    req = request.get_data()
    dict_req = wrangle_js_data(req)
    arra_req = toArray(dict_req)
    print(arra_req)
    return '0' # doesn't matter what returns here as what we return to front end doesn't matter




# Helper Methods
def wrangle_js_data(bytes): # turns bytes of data from request.get_data() into class dict
    string = str(bytes)
    ind1 = string.find('{')
    ind2 = string.find('}')
    string = string[ind1:(ind2+1)]
    dict = json.loads(string) # turns {string} into a dict
    return dict

def toArray(dict): # returns array [string event name, string deadline, integer hours, boolean blocks]
    int1 = int(dict['hours'])
    bool1 = bool(dict['blocks'])
    a1 = [dict['event_name'], dict['deadline'], int1, bool1] # turns dictionary elements to array
    return a1


if __name__ == '__main__':
    app.run()
