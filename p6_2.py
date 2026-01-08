import numpy as np
from sklearn.linear_model import LinearRegression
import pandas as pd

import matplotlib.pyplot as plt

def plott():
    df = pd.read_csv("weather_data.csv")
    print(df)
    X = df[["temp"]]
    Y = df["humidity"]

    model = LinearRegression().fit(X,Y)

    prediction = model.predict([[34]])
    print("Prediction= ", prediction)

    plt.scatter(X, Y, color="Blue", label="Humid")
    plt.plot(X, model.predict(X), color="Red", label="Best Fit Line")

    plt.xlabel("temp")
    plt.ylabel("Humid")
    plt.legend()
    plt.show()

plott()