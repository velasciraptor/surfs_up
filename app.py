from flask import Flask, jsonify
import datetime as dt
import numpy as np
import pandas as pd

# set up for SQLite
engine = create_engine("sqlite:///hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect=True)

# createvars to hold the classes
Measurement = Base.classes.measurement
Station = Base.classes.station

# create a session so you can query
session = Session(engine)

# create a Flask Application labeled "app"
app = Flask(__name__)

# create a welcome route
@app.route('/')
def hello_world():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')


