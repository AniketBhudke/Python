import numpy as np
# a=[11,23,2,3,4,5,6,77,90]
# s=np.sort(a)
# print(s)

#2-d array
a=np.array([11,23,2,3,4,5,6,77,90])
a.shape=(3,3)
print(a)
s=np.sort(a,axis=0)#column
print(s)

a=np.array([11,23,2,3,4,5,6,77,90])
a.shape=(3,3)
s=np.sort(a,axis=1)#row
print(s)