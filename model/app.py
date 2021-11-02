from flask import Flask, request
import json
import numpy as np
import pandas as pd
import pickle
from .validator import process_input


# TO LOAD MODEL FROM FILE
with open("model/clf.pkl", "rb") as model_file:
    classifier = pickle.load(model_file)

app = Flask(__name__)


@app.route("/", methods=['GET'])
def welcome_app():
    return ('Welcome to Boston house price prediction API'), 200


@app.route("/predict", methods=["POST"])
def predict() -> str:
    '''
      predicts the model in created route 
    '''
    try:
        input_params = process_input(request.data)
        print(input_params)
        predictions = classifier.predict(input_params)
        

        return json.dumps({"prediction": predictions.tolist()})    
    except (KeyError, json.JSONDecodeError, AssertionError) as error:
        return json.dumps({"error": str(error)}), 400
    except Exception as error:
        return json.dumps({"error": str(error)}), 500


if __name__ == "__main__":
    app.run()
