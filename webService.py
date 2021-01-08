# Numerical arrays
import numpy as np
# data Frames
import pandas as panda
# Plotting
import matplotlib.pyplot as plt
import tensorflow as tensor
# Neural networks.
import tensorflow.keras as kr
from sklearn.model_selection import train_test_split
from tensorflow.keras import layers
from tensorflow.keras.layers import Dense
from tensorflow.keras.optimizers import SGD,Adam

from flask import Flask, jsonify
from flask import request
import json

app = Flask(__name__)

#route html
@app.route('/')
def runner():
    return app.send_static_file('home.html')


#post request
#This route retrieves data from the POST request made in the home.html page
#This uses JSON library to make it into a JSON object
#This is used for the predict model
#Casted as string
@app.route('/predict', methods=['POST'])
def parse_request():
    jsonData = json.loads(request.data) 
    ppmodel = kr.models.load_model('powerproduction.h5')
    predict = ppmodel.predict([float(jsonData['speed'])])
    flatten = predict.flatten() # flattened 2D array into 1D
    return str(flatten[0])