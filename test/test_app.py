from flask import Flask, request
# from werkzeug.test import Client
from model.app import app
from model.validator import process_input
import json
import pytest


client = app.test_client()

def test_base_route_welcome():
    url = "/"
    response = client.get(url)
    assert response.get_data() == b'Welcome to Boston house price prediction API'
    assert response.status_code == 200 

def test_post_route_process_input():
    data = json.dumps({"inputs":
                        {"CRIM": [3.6781], "ZN": [1], "INDUS": [18.1], "CHAS":[5], "NOX": [0.74] , "RM": [5.935], "AGE": [7.9], 
                        "DIS": [1.8206],"RAD": [24], "TAX": [666], "PTRATIO": [20.2], "B": [68.9], "LSTAT": [34.02]}})
    process_input(data)
   

def test_post_route_prediction():
    response = app.test_client().post("/predict",
        data=json.dumps({"inputs":{"CRIM": [3.6781], "ZN": [1], "INDUS": [18.1], "CHAS":[5], "NOX": [0.74] , "RM": [5.935], "AGE": [7.9], 
                        "DIS": [1.8206],"RAD": [24], "TAX": [666], "PTRATIO": [20.2], "B": [68.9], "LSTAT": [34.02]}}),
        content_type="application/json") 
    assert response.status_code == 200
