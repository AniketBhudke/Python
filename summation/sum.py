import numpy as np
# a=np.array([11,23,33,45,56,7,8,9,80]).reshape(3,3)
# b=np.array([11,23,33,45,560,70,80,80,90]).reshape(3,3)
# print(a)
# print("-----------------------------------")
# print(a)
# print("-----------------------------------")

# c=np.add(a,b)
# print(c)

# a=np.array([11,23,33,45,56,7,8,9,80])
# b=np.array([11,23,33,45,560,70,80,80,90])
# c=np.sum([a,b],axis=1)
# print(c)

# import numpy as np
# arr = np.array([[1,2,3],[3,4,5]])
# x = np.prod(arr,axis=0) # Here axis=0 Represents Column Product
# print(x)

# arr = np.array([[1,2,3],[3,4,5],[2,3,5]])
# print("Content of arr")
# print(arr)
# print("-------------------------")
# x = np.cumprod(arr,axis=1) # Here axis=1 Represents Cumulative Row Product 
# print(x)


import numpy as np
arr = np.array([[1,2,3],[3,4,5],[2,3,5]])
print("Content of arr")
print(arr)
print("-------------------------")
x = np.cumprod(arr,axis=0) # Here axis=0 Represents Cumulative Column Product
print(x)
