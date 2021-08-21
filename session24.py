import numpy as np

array_1_d = np.array([1, 2, 3, 4, 5])
print(array_1_d)
print(array_1_d.ndim)
print(array_1_d.nbytes)
print(array_1_d.shape)
print(array_1_d.data)

array_2_d = np.array([[1, 2, 3],
                     [4, 5, 6, 4],
                     [7, 8]])
print(array_2_d)
print(array_2_d.ndim)
print(array_2_d.shape)

