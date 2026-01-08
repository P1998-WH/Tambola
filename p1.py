import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import accuracy_score, classification_report


thr = 0.33

df = pd.read_csv("weather_data.csv")
df["DATE"] = pd.to_datetime(df["DATE"], errors="coerce")
df = df.dropna(subset=["DATE"]).sort_values("DATE")


df["rain"] = (df["precip"] > thr).astype(int)
X = df[["temp", "windspeed", "humidity", "sealevelpressure"]]
y = df["rain"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42,
                                                    stratify=y)
pd.set_option("display.max_rows", None)
pd.set_option("display.max_columns", None)
pd.set_option("display.width", None)

dates = df["DATE"].to_list()
temps = df["temp"].to_numpy()
winds = df["windspeed"].to_numpy()
humidity = df["humidity"].to_numpy()
pressure = df["sealevelpressure"].to_numpy()
precip = df["precip"].to_numpy()

print(df[["DATE", "temp", "windspeed", "humidity", "sealevelpressure", "precip"]])

# date = latest["DATE"]
# temp = latest["temp"]
# wind = latest["windspeed"]
# Humidity = latest["humidity"]
# Barometer = latest["sealevelpressure"]
# percipitation = latest["precip"]

# print(f"Date: {date}")
# print(f"Temperature: {temp}")
# print(f"Wind Speed: {wind}")
# print(f"Humidity: {Humidity}")
# print(f"Barometric Pressure: {Barometer}")
# print(f"Precipitation: {percipitation}")