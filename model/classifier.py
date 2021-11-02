import numpy as np
import pandas as pd
import pickle
from sklearn.datasets import load_boston
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression


data_url = "http://lib.stat.cmu.edu/datasets/boston"
raw_df = pd.read_csv(data_url, sep="\s+", skiprows=22, header=None)
boston_data = np.hstack([raw_df.values[::2, :], raw_df.values[1::2, :2]])
target = raw_df.values[1::2, 2]


data = pd.DataFrame(boston_data, 
                    columns=['CRIM', 'ZN', 'INDUS', 'CHAS', 'NOX', 'RM', 'AGE', 
                             'DIS', 'RAD', 'TAX', 'PTRATIO', 'B', 'LSTAT'])

X_train, X_test, y_train, y_test = train_test_split(data, target)

clf = LinearRegression()
clf.fit(X_train, y_train)
predicted = clf.predict(X_test)
expected = y_test

# TO SAVE MODEL TO FILE
with open("clf.pkl", "wb") as f:
    pickle.dump(clf, f) 
