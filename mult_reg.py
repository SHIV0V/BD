import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

area     = [800, 900, 1000, 1100, 1200, 1300, 1400, 1500, 1650, 1800]
bedrooms = [2, 2, 3, 3, 3, 3, 4, 4, 4, 5]
price    = [48, 60, 79, 84, 90, 99, 110, 120, 132, 150]

X = list(zip(area, bedrooms))
model = LinearRegression().fit(X, price)
pred = model.predict(X)

ax = plt.figure().add_subplot(projection="3d")
ax.scatter(area, bedrooms, price, color="blue", label="Actual")
ax.scatter(area, bedrooms, pred, color="red", label="Predicted")

ax.set_xlabel("Area")
ax.set_ylabel("Bedrooms")
ax.set_zlabel("Price")
ax.legend()
plt.show()
print("Coefficients:", model.coef_)
print("Intercept:", round(model.intercept_, 2))
print("Predictions:", pred.round(2))