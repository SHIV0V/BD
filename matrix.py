import numpy as np

a = np.array([[1,2],[3,4]])
b = np.array([[5,6],[7,8]])

print("Addition:\n",a+b)
print("Subtraction:\n",a-b)
print("Multiplication:\n",a*b)
print("Matrix Product:\n",a@b)
print("Transpose:\n",a.T)