from flask import Flask
import datetime as dt
import numpy as np
import pandas as pd

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello world'
