#array
#arange()
#zeros()
#ones()
#eye()
#identity
#linspace()
#full
#hstack()
#vstack()

#random module
##randint-----int
#randn()---negative and positive
#rand()----float 0 to 1
#choice()---
#normal()----loc,scale
#uniform------floating by user choice
#shuffle--


#_------------------------------------------------------------------------------------------------------------------------
#filtering data in numpy
#where() and extract()
#_------------------------------------------------------------------------------------------------------------------------
#where()----returns the indexs
# import numpy as np
# arr = np.array([10, 20, 30, 40, 50])
# result = np.where(arr > 30)
# print(result)  # Output: [0 0 0 1 1]

#extract()----retrurn the value
# import numpy as np

# arr = np.array([10, 20, 30, 40, 50])
# result = np.extract(arr > 30, arr)
# print(result)  # Output: [40 50]
#_------------------------------------------------------------------------------------------------------------------------

#numpy.nditer()
#1-d array
# import numpy as np
# a=np.arange(11,19)
# for i in np.nditer(a):
#     print(i)

#2-d array
# import numpy as np
# a=np.arange(10,19).reshape(3,3)
# print(a)
# for i in np.nditer(a):
#     print(i)

# #3-d array
# import numpy as np
# a=np.arange(10,22).reshape(2,3,2)
# print(a)
# for i in np.nditer(a):
#     print(i)    
#_------------------------------------------------------------------------------------------------------------------------

#np.ndenumerate()
#1-d array
# import numpy as np
# a=np.arange(11,19)
# for ind,val in np.ndenumerate(a):
#     print(ind,val)

#2-d array
# import numpy as np
# a=np.arange(10,19).reshape(3,3)
# print(a)
# for ind,val in np.ndenumerate(a):
#     print(ind,val)

#3-d array
# import numpy as np
# a=np.arange(10,22).reshape(2,3,2)
# print(a)
# for ind,val in np.ndenumerate(a):
#     print(ind,val)    
#_------------------------------------------------------------------------------------------------------------------------

#copy() and view()
#copy() ---copy  karate pn tya ch effect nhi hot kashya vr
# import numpy as np
# a=np.arange(10,20)
# b=a.copy()
# a[0]=789
# print("a:",a)
# print("b",b)


#view()-----ya mde data change hote
# import numpy as np
# a=np.arange(10,20)
# b=a.view()  
# a[0]=789
# print("a:",a)
# print("b",b)    
#_------------------------------------------------------------------------------------------------------------------------

#flattern() and ravel()
#flattern()---like copy pn 1-d mde coveert krte 

# import numpy as np
# a=np.array([[1,2,3],[4,5,6]])
# b=a.flatten()
# a[0][1]=77
# print(a)
# print(b)


#revel()------change hote doni ya mde 
# import numpy as np
# a=np.array([[1,2,3],[4,5,6]])
# b=a.ravel()
# a[0][1]=77
# print(a)
# print(b)
#---------------------------------------------------------------------------------------------------------------

#Arithmatic operations
#Add,subtract,multiply,dot or matmul,divide,floor_divide,mod,power

#add
# import numpy as np
# a=np.array([1,2,3,4,5])
# b=np.array([6,7,8,9,10])
# c=np.add(a,b)
# print(c)

# import numpy as np
# a=np.array([1,2,3,4,5])
# b=np.array([6,7,8,9,10])
# c=a+b
# print(c)

#substract()
# import numpy as np
# a=np.array([1,2,3,4,5])
# b=np.array([6,7,8,9,10])
# c=np.subtract(a,b)
# print(c)

# import numpy as np
# a=np.array([1,2,3,4,5])
# b=np.array([6,7,8,9,10])
# c=a-b
# print(c)

#multiply----multiple of two array
# import numpy as np
# a=np.array([1,2,3,4,5])
# b=np.array([6,7,8,9,10])
# c=np.multiply(a,b)
# print(c)

# import numpy as np
# a=np.array([1,2,3,4,5])
# b=np.array([6,7,8,9,10])
# c=a*b
# print(c)

#dot() and matmul()-----multiplication of whole matrix
# import numpy as np
# a=np.array([1,2,3,4,5])
# b=np.array([6,7,8,9,10])
# c=np.dot(a,b)
# print(c)

# import numpy as np
# a=np.array([1,2,3,4,5])
# b=np.array([6,7,8,9,10])
# c=np.matmul(a,b)
# print(c)


# import numpy as np
# a=np.array([1,2,3,4,5])
# b=np.array([6,7,8,9,10])
# c=a*b
# print(c)

#divide
# import numpy as np
# a=np.array([1,2,3,4,5])
# b=np.array([6,7,8,9,10])
# c=np.divide(a,b)
# print(c)

#floor_divide
# import numpy as np
# a=np.array([1,2,3,4,5])
# b=np.array([6,7,8,9,10])
# c=np.floor_divide(b,a)
# print(c)

# import numpy as np
# a=np.array([1,2,3,4,5])
# b=np.array([6,7,8,9,10])
# c=np.mod(b,a)
# print(c)

# import numpy as np
# a=np.array([1,2,3,4,5])
# b=np.array([6,7,8,9,10])
# c=np.power(b,a)
# print(c)


#--------------------------------------------------------------------------------------------------------

# static method
#amax,amin,mean,median,var,std

#amax
import numpy as np
# a=np.array([1,2,3,4,5])
# print(np.amax(a))

# a=np.array([1,2,3,4,5,6]).reshape(3,2)
# print(a)
# print(np.amax(a))

#column=0
# a=np.array([1,2,3,4,5,6]).reshape(3,2)
# print(np.amax(a,axis=0))

# row=1
# a=np.array([1,2,3,4,5,6]).reshape(3,2)
# print(np.amax(a,axis=1))

#amin
# a=np.array([1,2,3,4,5,6]).reshape(3,2)
# print(np.amin(a))

# #row=1
# a=np.array([1,2,3,4,5,6]).reshape(3,2)
# print(np.amin(a,axis=1))

#column=0
# a=np.array([1,2,3,4,5,6]).reshape(3,2)
# print(np.amin(a,axis=0))

#mean
# a=np.array([1,2,3,4,5,6]).reshape(3,2)
# print(np.mean(a))

#row=1
# a=np.array([1,2,3,4,5,6]).reshape(3,2)
# print(np.mean(a,axis=1))

#column=0
# a=np.array([1,2,3,4,5,6]).reshape(3,2)
# print(np.mean(a,axis=0))

#median
# a=np.array([1,2,3,4,5,6])
# print(np.median(a))

#row=1
# a=np.array([1,2,3,4,5,6]).reshape(3,2)
# print(np.median(a,axis=1))

#column=0
# a=np.array([1,2,3,4,5,6]).reshape(3,2)
# print(np.median(a,axis=0))


# a=np.array([1,2,3,4,5,6]).reshape(3,2)
# print(np.var(a))

#row=1
# a=np.array([1,2,3,4,5,6]).reshape(3,2)
# print(np.var(a,axis=1))

#column=0
# a=np.array([1,2,3,4,5,6]).reshape(3,2)
# print(np.var(a,axis=0))

#std

# a=np.array([1,2,3,4,5,6]).reshape(3,2)
# print(np.std(a))

# a=np.array([1,2,3,4,5,6]).reshape(3,2)
# print(np.std(a,axis=1))

# a=np.array([1,2,3,4,5,6]).reshape(3,2)
# print(np.std(a,axis=0))

#-----------------------------------------------------------------------------------------------------------------
#append(),update(),delete()
# a=np.array([1,2,3,4,5,6])
# a=np.append(a,22)
# print(a)

#row=0
# a=np.array([1,2,3,4,5,6]).reshape(3,2)
# print(a)
# b=np.append(a,[[2,22]],axis=0)
# print(b)

#column=1
# a=np.array([1,2,3,4,5,6]).reshape(3,2)
# print(a)
# b=np.append(a,[[2],[22],[22]],axis=1)
# print(b)

#insert
# a=np.array([1,2,3,4,5,6])
# print(a)
# b=np.insert(a,3,64)
# print(b)

# a=np.array([1,2,3,4,5,6]).reshape(3,2)
# print(a)
# b=np.insert(a,1,[[11,23]],axis=0)
# print(b)

# a=np.array([1,2,3,4,5,6]).reshape(3,2)
# print(a)
# b=np.insert(a,1,[[11,23,45]],axis=1)
# print(b)

#delete()
# a=np.array([1,2,3,4,5,6])
# print(a)
# a=np.delete(a,3)
# print(a)

# a=np.array([1,2,3,4,5,6]).reshape(3,2)
# print(a)
# a=np.delete(a,1,axis=0)
# print(a)

# a=np.array([1,2,3,4,5,6]).reshape(3,2)
# print(a)
# a=np.delete(a,1,axis=1)
# print(a)
# --------------------------------------------------------------------------------------------------------------------

#numpy linear algebra

#dot(),inner(),outer(),det(),solve(),inv(),trace()

#dot()
# import numpy as np
# a=np.array([1,2,3,4,5,6])
# b=np.array([7,8,9,10,11,12])
# c=np.dot(a,b)
# print(a)
# print(b)
# print(c)

# import numpy as np
# a=np.array([1,2,3,4,5,6])
# b=np.array([7,8,9,10,11,12])
# c=np.inner(a,b)
# print(a)
# print(b)
# print(c)

# import numpy as np
# a=np.array([1,2,3,4,5,6])
# b=np.array([7,8,9,10,11,12])
# c=np.outer(a,b)
# print(a)
# print(b)
# print(c)

import numpy as np
a=np.array([[1,2],[4,6]])
c=np.linalg.det(a)
print(c)
# import numpy as np

# # Define a square 2x2 matrix
# a = np.array([[1, 2], [3, 4]])

# # Calculate the determinant
# determinant = np.linalg.det(a)

# print(determinant)
