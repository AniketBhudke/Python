import numpy as np
# #ARRAY
# a=np.array([1,2,3,4,5,6,7,8,9]).reshape(3,3)
# print(a)
# print("Dimension oif the matrix =",a.ndim)
# print("Shape of the matrix =",a.shape)
# print("Size of the matrix=",a.size)
# print("Type of array=",type(a))
# print("Intyernal Elment type=",a.dtype)


# import numpy as np
# # #Arange
# a=np.arange(9).reshape(3,3)
# print(a)
# print("Dimension oif the matrix =",a.ndim)
# print("Shape of the matrix =",a.shape)
# print("Size of the matrix=",a.size)
# print("Type of array=",type(a))
# print("Intyernal Elment type=",a.dtype)


# a=np.arange(1,10).reshape(3,3)
# print(a)
# print("Dimension oif the matrix =",a.ndim)
# print("Shape of the matrix =",a.shape)
# print("Size of the matrix=",a.size)
# print("Type of array=",type(a))
# print("Intyernal Elment type=",a.dtype)

#Zeros
# import numpy as np
# a=np.zeros(9).reshape(3,3)
# print(a)
# print("Dimension oif the matrix =",a.ndim)
# print("Shape of the matrix =",a.shape)
# print("Size of the matrix=",a.size)
# print("Type of array=",type(a))
# print("Intyernal Elment type=",a.dtype)


#ones
# a=np.ones(9).reshape(3,3)
# print(a)
# print("Dimension oif the matrix =",a.ndim)
# print("Shape of the matrix =",a.shape)
# print("Size of the matrix=",a.size)
# print("Type of array=",type(a))
# print("Intyernal Elment type=",a.dtype)

# full
# import numpy as np
# a=np.full(9,88,dtype=int).reshape(3,3)
# print(a)
# print("Dimension oif the matrix =",a.ndim)
# print("Shape of the matrix =",a.shape)
# print("Size of the matrix=",a.size)
# print("Type of array=",type(a))
# print("Intyernal Elment type=",a.dtype)

#linspace
# import numpy as np
# a,rv=np.linspace(1,10,44,endpoint=False,retstep=True)
# print(a)
# print(rv)
# print("Dimension oif the matrix =",a.ndim)
# print("Shape of the matrix =",a.shape)
# print("Size of the matrix=",a.size)
# print("Type of array=",type(a))
# print("Intyernal Elment type=",a.dtype)

#identity
# import numpy as np
# a=np.identity(9)
# print(a)
# print("Dimension oif the matrix =",a.ndim)
# print("Shape of the matrix =",a.shape)
# print("Size of the matrix=",a.size)
# print("Type of array=",type(a))
# print("Intyernal Elment type=",a.dtype)

# eye
# import numpy as np
# a=np.eye(5,8,k=2)
# print(a)
# print("Dimension oif the matrix =",a.ndim)
# print("Shape of the matrix =",a.shape)
# print("Size of the matrix=",a.size)
# print("Type of array=",type(a))
# print("Intyernal Elment type=",a.dtype)

#hstack--horizontal
import numpy as np
# a=np.arange(1,10).reshape(3,3)
# b=np.arange(11,20).reshape(3,3)
# z=np.hstack((a,b))
# print(z)

#vstack---vertical
a=np.arange(1,13).reshape(2,3,2)
b=np.arange(11,23).reshape(2,3,2)
z=np.hstack((a,b))
print(z)


