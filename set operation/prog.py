import numpy as np
# arr=[1,11,22,22,33,45,67,88,99,99,90]
# a=np.array(arr)
# s=np.unique(a)
# print(type(s),s)

# a=np.array([11,22,33,44,55,66,77,88,9,9,22,33,44,9])
# b=np.array([1,2,3,4,5,6,7,8,9])
# c=np.union1d(a,b)
# print(c)


# a=np.array([11,22,33,44,55,66,77,88,9,9,22,33,44,9])
# b=np.array([1,1,2,3,4,5,6,7,8,9,9])
# c=np.intersect1d(a,b,assume_unique=False)
# print(c)

set1 = np.array([1, 2,2, 3, 4])
set2 = np.array([3, 4, 5, 6])

newarr = np.setdiff1d(set1, set2, assume_unique=True)

print(newarr)


# import numpy as np

# set1 = np.array([1,2,2, 3, 4])
# set2 = np.array([3, 4, 5, 6])

# newarr = np.setxor1d(set1, set2, assume_unique=True)

# print(newarr)
