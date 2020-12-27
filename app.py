from flask import Flask, request, jsonify
import os
from datetime import datetime
import numpy as np

from predict import predict_prob
from disease_description import disease_description


app = Flask(__name__)
UPLOAD_FOLDER = './UPLOAD_FOLDER/'


@app.route('/')
def hello():
    return 'Hello'


@app.route('/disease/heart/test', methods=['POST', 'GET'])
def get_prob():
    

if __name__ == '__main__':
      app.run(port=8000)
