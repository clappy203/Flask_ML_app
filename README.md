# Flask_ML_app 
# House Price Prediction 

##Description
This is a simple API that predicts house prices in Boston based on the inputs given in the post request.

##Getting Started
Using this API is very simple. The API can be found on [Petra's API](https://e2eml-database.herokuapp.com/)and has just one useful endpoint: [predict](https://e2eml-database.herokuapp.com/predict)

The predict endpoint takes only POST requests and request made to the endpoint should come with inputs as part of the request data.

The inputs should be a list containing 13 numbers. e.g    
  
    import requests
    import json

    resp = requests.post("https://e2eml-database.herokuapp.com/predict", 
                       data=json.dumps({"inputs":
      [[3.6781, 1, 18.1, 5, 0.74 , 5.935, 7.9, 1.8206,24, 666, 20.2,  68.9, 34.02]]
    }))
    print(resp.text)
    
The API can also be tested using [Thunder Client](https://www.thunderclient.io/)

![Thunderclient](https://user-images.githubusercontent.com/63512506/136703546-295fb3e6-3f14-4055-85d6-635bf3dfc61a.png)

    
    

#LICENSE
The MIT License - Copyright (c) 2021 Cla-petra Omaku
