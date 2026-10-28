import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y = [10, 20, 30, 40]

x1 = [1, 2, 3, 4]
y1 = [10, 2, 55, 20]

plt.subplot(1, 2, 1)
plt.plot(x, y)
plt.title("Line Plot")

plt.subplot(1, 2, 2)
plt.plot(x1, y1)
plt.title("Line Plot")

plt.show()