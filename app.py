
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
    work2 = str(req)
    #ind1 = str(req).find('{')
    #ind2 = str(req).find('}')
    #work = str(req)[ind1:(ind2 + 1)]
    # print(work2)
    ind1 = work2.find('{')
    ind2 = work2.find('}')
    work = work2[ind1:(ind2 + 1)]
    print(work)
    return '0' # doesn't matter what returns here as what we return to front end doesn't matter




# Helper Methods



if __name__ == '__main__':
    app.run()
