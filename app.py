
import pandas as pd
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)
app.config["DEBUG"] = True # set to True while debugging

# code goes here

if __name__ == '__main__':
    app.run()
