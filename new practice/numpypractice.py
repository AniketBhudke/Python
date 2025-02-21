import numpy as np
# a=np.array([11,12,13,14]).reshape(2,2)
# b=np.array([11,12,1,14]).reshape(2,2)
# c=np.dot(b,a)
# print(c)

# b=np.array([11,12,1,14]).reshape(2,2)
# c=np.std(b)
# print(c)

# a=np.array([[11,12],[34,56]])
# b=np.array([[11,12],[3,6]])
# c=np.linalg.det(a)
# print(c)

# a = np.array([1.7, 2.3, 3.9, -0.5])
# b=np.floor(a)
# print(b)
# c=np.ceil(a)
# print(c)

a=[10,33,56,78,96,5,4,2]
c=np.diff(a,n=5)
print(c)