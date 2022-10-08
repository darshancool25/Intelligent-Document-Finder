# Import libraries
import math
import numpy as np
import pandas as pd
from flask import Flask, request, jsonify
import pickle
from sklearn.datasets import load_diabetes
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier

app = Flask(__name__)

def get_max_two_recommendations(recommendations):
    res = []
    max1,max2=-1,-1
    for recommendation in recommendations:
        num = recommendation[2]
        if (max1 < num):
            max2 = max1
            max1 =num
        elif(max2 < num):
            max2 = num
    for recommendation in recommendations : 
        if recommendation[2] == max1 or recommendation[2] = max2:
            res.append(recommendation)
    return res
        

def find_recommendations(param1, recommendations):
    pickled_model = pickle.load(open('model.pkl', 'rb'))
    #TODO - Standard scalar and OHE
    result = pickled_model.predict(param1)
    recommendations = clean_result(result)

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