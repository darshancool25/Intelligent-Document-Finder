# Import libraries
import math
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/")
def Home():
    return "<p>This is Home Page!</p>"

@app.route('/getfile', methods=['GET','POST'])
def getfile():
    if request.method == 'POST':
        result = request.form['myfile']
    else:
        result = request.args.get['myfile']
    return result

@app.route('/getRecommendation')
def getRecommendation():
    args = request.args
    param1 = str(args.get('param1'))
    # recommendations for the account
    recommendations = []
    find_recommendations(param1, recommendations)
    recommendations = get_max_two_recommendations(recommendations)
    responseObjList = []
    for data in recommendations : 
        responseObj = {}
        responseObj['text'] = data['text']
        responseObj['rank'] = data['rank']
        responseObjList.append(responseObj)
    return jsonify(responseObjList)


if __name__ == '__main__':
    app.run(port=5001, debug=True)
