import numpy as np

arr=np.array([1,2,3,4,5])

arr.size  #returns number of elements in arr 

arr.shape  #returns dimensions of arr (rows, columns)
 
arr.dtype  #returns type of elements in arr
 
arr.astype(dtype)  #convert arr elements to type dtype
 
arr.tolist()  #convert arr to a Python list 

np.info(np.eye)  #view documentation for np.eye
