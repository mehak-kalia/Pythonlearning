import numpy as np
X = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9],
              [10, 11, 12]])

print("X is :")
print(X)
print(X.shape)

vector = np.array([1, 0, 1])

print("vector is:")
print(vector)

Y = np.empty_like(X)
print("y is")
print(Y)
print(Y.shape)

for i in range(len(X)):
    Y[i, :] = X[i, :] + vector

print(Y)

print(X + vector)