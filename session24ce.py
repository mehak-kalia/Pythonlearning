import numpy as np
A = np.array([
    [1, 2],
    [3, 4]
])

B = np.array([
    [5, 6],
    [7, 8]
])

print("SUM is:")
SUM = A + B
print(SUM)
print(SUM.shape)
print("MUL is:")
MUL = A * B
print(MUL)
print(MUL.shape)

DIV = A/B
print(DIV)

exp = np.exp(A)
print("EXP of A is: ")
print(exp)