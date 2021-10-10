from flask import Flask, request
import json
import numpy as np
import pandas as pd
import pickle


# DEFINING PATH TO THE SAVED MODEL'S .pkl FILE
SAVED_MODEL_PATH = "clf.pkl"

# LOADING THE CLASSIFIER FROM FILE
classifier = pickle.load(open(SAVED_MODEL_PATH, "rb"))

app = Flask(__name__)

@app.route("/", methods=['GET'])
def welcome_app():
    return json.dumps({"message": "Welcome to model prediction app"}), 200


def __process_input(request_data: str) -> np.array:
    '''
    Creates a processing function to transform inputs to expected outcome
    '''
    parsed_body = np.asarray(json.loads(request_data)["inputs"])
    assert len(parsed_body.shape) == 2, "'inputs' must be a 2-d array"
    return parsed_body


@app.route("/predict", methods=["POST"])
def predict() -> str:
    '''
      predicts the model in created route 
    '''
    try:
        input_params = __process_input(request.data)
        predictions = classifier.predict(input_params)

        return json.dumps({"model's predictions": predictions.tolist()})
    except (KeyError, json.JSONDecodeError, AssertionError) as error:
        return json.dumps({"error": error}), 400
    except Exception as error:
        return json.dumps({"error": error}), 400
