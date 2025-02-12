# Split numpy array using ---->numpy.split()
# Split numpy array using-----> numpy.array_split()
# Splitting NumPy 2D Arrays
# 	Split numpy array using---> numpy.vsplit()
# 	Split numpy array using---> numpy.hsplit()
# 	Split numpy arrayusing----> numpy.dsplit()


# Split numpy array using ---->numpy.split()---divide in equal part
# import numpy as np
# a=np.array([1,2,3,4,5,6,7,8,9])
# s=np.split(a,3)
# print(s)

# Split numpy array using-----> numpy.array_split()-------------------divide in unequal part
# import numpy as np
# a=np.array([1,2,3,4,5,6,7,8,9])
# s=np.array_split(a,4)
# print(s)

# 	Split numpy array using---> numpy.split()
# import numpy as np
# a=np.array([1,2,3,4,5,6,7,8,9]).reshape(3,3)
# print(a)
# print("--------------------------")
# s=np.split(a,3,axis=0)#0 row
# print(s)

# import numpy as np
# a=np.array([1,2,3,4,5,6,7,8,9]).reshape(3,3)
# print(a)
# print("--------------------------")
# s=np.split(a,3,axis=1)#0 column
# print(s)


# Split numpy array using---> numpy.vsplit()
# import numpy as np
# a=np.array([1,2,3,4,5,6,7,8,9]).reshape(3,3)
# print(a)
# print("--------------------------")
# s=np.vsplit(a,3)#0 column
# print(s)

# import numpy as np
# a=np.array([1,2,3,4,5,6,7,8,9]).reshape(3,3)
# print(a)
# print("--------------------------")
# s=np.hsplit(a,3)#0 column
# print(s)



# 	Split numpy arrayusing----> numpy.dsplit()
# import numpy as np
# a=np.array([1,2,3,4,5,6,7,8,9]).reshape(3,3)
# print(a)
# print("--------------------------")
# s=np.hsplit(a,3)#0 column
# print(s)


# import numpy as np

# # Creating an example 3D array
# original_3d_array = np.arange(24).reshape(2, 3, 4)

# # Splitting along axis=2 (third axis)
# result = np.dsplit(original_3d_array, 2\)

# print("Original 3D Array:")
# print(original_3d_array)
# print("\nResult after numpy.dsplit():")
# print(result)
