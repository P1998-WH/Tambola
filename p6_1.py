import numpy as np
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

hours = np.array([1,2,3,4,5]).reshape(-1,1)
score = np.array([40, 50, 60, 70, 80])

model = LinearRegression()
model.fit(hours, score)

prediction = model.predict([[6]])
print("Prediction Score: ", prediction)

plt.scatter(hours, score, color="Blue", label="Actual Data")
plt.plot(hours, model.predict(hours), color="Red", label="Best Fit line")

plt.xlabel("Hours")
plt.ylabel("Score")
plt.legend()
plt.show()
# “If someone studies 6 hours, what score do we expect?”
# 90. because data is increasing linearly. for each hour it increase by 10. So the answer is predicted 90 as there is a pattern identified. Similar to 
# our accumulator method.
# Day 6 Reflection:
# 1) What is the best-fit line in my own words?
# Best fit line is a line that is closest to the line with values closest.
# 2) What did the model "learn"?
# model learned the value pattern
# 3) What confused me?
# I was thinking how can I implement a csv file value here. Suppose i have a series of date and humidity so how can i fetch them from the file.