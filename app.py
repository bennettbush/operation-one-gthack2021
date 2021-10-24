
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

@app.route('/frontEnd/allocate', methods=['GET','POST']) # link to front end
def time_allocation():
    req = request.get_data()
    print(type(req))
    print("hello")
    return '0' # doesn't matter what returns here as what we return to front end doesn't matter




# Helper Methods



if __name__ == '__main__':
    app.run()
