import matplotlib.pyplot as plt
import pickle
from sklearn.datasets import load_boston
data = load_boston()


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(data.data, data.target)

from sklearn.linear_model import LinearRegression
clf = LinearRegression()
clf.fit(X_train, y_train)
predicted = clf.predict(X_test)
expected = y_test

# TO SAVE MODEL TO FILE
with open("clf.pkl", "wb") as f:
    pickle.dump(clf, f) 

