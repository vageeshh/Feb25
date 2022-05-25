import numpy
import pickle

import numpy as np
from flask import Flask, render_template, request, jsonify
import sklearn

app = Flask(__name__)

@app.route('/')
def Home():
    return render_template('')


@app.route('',methods=['POST','GET'])
def results():
    bedrooms = float(requests.form['bedrooms'])
    bathrooms=float(requests.form['bathrooms'])
    sqft_living=float(requests.form['sqft_living'])
    sqft_lot=float(requests.form['sqft_lot'])
    floors=float(requests.form['floors'])
    waterfront=float(requests.form['waterfront'])
    view=float(requests.form['view'])
    condition=float(requests.form['condition'])
    sqft_above=float(requests.form['sqft_above'])
    sqft_basement=float(requests.form['sqft_basement'])
    yr_built=float(requests.form['yr_built'])
    yr_renovated=float(requests.form['yr_renovated'])

    X = np.array([[bedrooms,bathrooms,sqft_living,sqft_lot,floors,waterfront,view,condition,sqft_above,sqft_basement,yr_built,yr_renovated]])
    model = pickle.load(open('model.pkl','rb'))
    Y_prediction = model.predict(X)
    return jsonify({'Model Prediction': float(Y_prediction)})

if __name__ =='__main__':
    app.run(debug = True, port: 1010)














   #,,,,,,,,,,,