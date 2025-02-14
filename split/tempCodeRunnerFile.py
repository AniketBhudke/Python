import numpy as np
a=np.array([1,2,3,4,5,6,7,8,9]).reshape(3,3)
print(a)
print("--------------------------")
s=np.vsplit(a,3)#0 column
print(s)
