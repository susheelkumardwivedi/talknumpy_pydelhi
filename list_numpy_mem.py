#program show memory consumption for both list and numpy
import numpy as np
import sys
import time

list_data=range(100000)
numpy_data=np.array(list_data)

list_mem=sys.getsizeof(1)*len(numpy_data)
numpy_mem=numpy_data.size*numpy_data.itemsize;
print('********************Memory*****************************')
print('Memory consume by python list',list_mem,'bytes')
print('Memory consume by numpy array',numpy_mem,'bytes')
if list_mem > numpy_mem:
    print('Numpy takes less memory and saved',list_mem-numpy_mem,'bytes')
else:
    print('Numpy takes less memory and saved',numpy_mem-list_mem,'bytes')
