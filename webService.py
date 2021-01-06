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
