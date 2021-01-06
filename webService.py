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

@app.route('/')
def runner():
    return app.send_static_file('home.html')

@app.route('/index', methods=['GET'])
def index():
    return app.send_static_file('index.html')


@app.route('/predict', methods=['POST'])
def parse_request():
    requestData = request.data
    jsonData = json.loads(requestData)
    speedPredict = float(jsonData['speed'])
    ppmodel = kr.models.load_model('powerproduction.h5')
    predict = ppmodel.predict([speedPredict])
    flatten = predict.flatten()
    print(flatten[0])
    return str(flatten[0])