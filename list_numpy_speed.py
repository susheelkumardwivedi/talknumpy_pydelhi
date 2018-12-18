# this program demonstrate speed of both list and numpy
# addition operation performed in 2 list and 2 numpy array of same size 
import numpy as np
import random
import time
list_1=range(1000000)
list_2=range(1000000)

array_1=np.array(list_1)
array_2=np.array(list_2)

start=time.time()
list_add=[x+y for x,y in zip(list_1,list_2)]
list_operation_time=(time.time()-start)*1000

start=time.time()
array_add=np.add(array_1,array_2)
array_operation_time=(time.time()-start)*100

print('*********************Speed****************************')
print('time taken by list',list_operation_time,'ms')
print('time taken by numpy array',array_operation_time,'ms')

if list_operation_time > array_operation_time:
    print('numpy is faster',list_operation_time-array_operation_time,'ms')
else:
    print('list is faster',array_operation_time-listoperation_time,'ms')

