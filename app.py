from flask import Flask, render_template, request

from helper.helper import predict

import json

app=Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict',methods=["POST"])
def prediction():
    symptoms = request.get_json()["data"]
    return predict(symptoms)


if __name__=="__main__":
    app.run(debug=True)