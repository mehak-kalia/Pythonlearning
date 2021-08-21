import numpy as np

#zeros_array = np.zeros((8, 8), dtype= int)
#zeros_array[1::2, 0::2]=1
#zeros_array[0::2, 1::2]=1
#print(zeros_array)

checkboard = np.ones((8, 8), dtype= int)
checkboard[0::2, 0::2]= 0
checkboard[1::2, 1::2]= 0
print(checkboard)
