import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

x = np.array([[1], [2], [3], [4]])
y = [2, 4, 6, 8]

model = LinearRegression()
model.fit(x, y)

print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)
print("Prediction:", model.predict([[5]]))

plt.scatter(x, y, label="Actual Data")
plt.plot(x, model.predict(x), color="red", label="Regression Line")
plt.xlabel("X Values")
plt.ylabel("Y Values")
plt.title("Linear Regression")
plt.legend()
plt.grid(True)
plt.show()