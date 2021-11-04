# House Price Prediction 

## **Description**
This is a simple API that predicts house prices in Boston based on the inputs given in the post request.

## **Getting Started**
Using this API is very simple. The API can be found on [Petra's API](https://e2eml-database.herokuapp.com/) 
and has just one useful endpoint: [predict](https://e2eml-database.herokuapp.com/predict)

The predict endpoint takes only POST requests and request made to the endpoint should come with inputs as part of the request data.

The inputs should be a list containing 13 numbers. e.g    
  
    import requests
    import json

    resp = requests.post("https://e2eml-database.herokuapp.com/predict", 
                       data=json.dumps({"inputs":
             {"CRIM": [3.6781], "ZN": [1], "INDUS": [18.1], "CHAS":[5], "NOX": [0.74] , "RM": [5.935],
              "AGE": [7.9], "DIS": [1.8206], "RAD": [24], "TAX": [666], 
              "PTRATIO": [20.2], "B": [68.9], "LSTAT": [34.02]}
              }))
    print(resp.text)
    
The API can also be tested using [Thunder Client](https://www.thunderclient.io/)

{
  "prediction": [
    20.979214650285158
  ]
}
    
    

## LICENSE
The MIT License - Copyright (c) 2021 Cla-petra Omaku
