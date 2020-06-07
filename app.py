from flask import Flask, jsonify
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, inspect
engine = create_engine("sqlite:///Resources/02-Homework_10-Advanced-Data-Storage-and-Retrieval_Instructions_Resources_hawaii.sqlite")
Base=automap_base()
Base.prepare(engine,reflect=True)
Measurement=Base.classes.measurement
Station=Base.classes.station
session=Session(engine)

result=session.query(Measurement).all()
result_app=[]
for rs in result:
    result_app.append(rs.__dict__)

app = Flask(__name__)

@app.route("/")
def home():
    return('''
    this are the routes listed
    Routes:

    ''')
@app.route("/api/v1.0/precipitation")
def precipitation():

    return (result_app)


if __name__ == "__main__":
    app.run(debug=True)