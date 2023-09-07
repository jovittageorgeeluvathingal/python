import numpy as np
​
arr = np.array([1, 3, 5, 7])
​
x = np.searchsorted(arr, [2, 4, 6])
​
print(x)
[1 2 3]
5
arr = np.array([1, 5, 5, 17])
​
x = np.searchsorted(arr, [2, 4, 6])
​
print(x)
[1 1 3]
,8
arr = np.array([1, 3, 5, 7])
​
x = np.searchsorted(arr, [2, 4, 6,8])
​
print(x)
[1 2 3 4]
import numpy as np
​
arr = np.array([1, 2, 3, 4], ndmin=3)
​
print(arr)
print('shape of array :', arr.shape)
[[[1 2 3 4]]]
shape of array : (1, 1, 4)
6
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
​
newarr = arr.reshape(6 , 2)
​
print(newarr)
[[ 1  2]
 [ 3  4]
 [ 5  6]
 [ 7  8]
 [ 9 10]
 [11 12]]
