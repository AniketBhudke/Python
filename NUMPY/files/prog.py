#writing the data in normal files
#it takes single data
# with open("D:\\PYTHON BACKEND\NUMPY\\files\\example.txt", 'w') as file:
#     file.write('Hello, World!\n')
#     file.write('This is a new line.')


# lines = ['Hello, World!\n', 'This is a new line.\n']
# with open('example.txt', 'w') as file:
#     file.writelines(lines)

# with open('example.txt', 'r') as file:
#     content = file.read()#read the daat line by line
#     print(content)

# with open('example.txt', 'r') as file:
#     content = file.readline()#read the daat line by line
#     print(content)

# #---------------------------------------------------------------------------------
# Creating a file: Use numpy.savetxt() to write a NumPy array to a normal text file.
# Reading a file: Use numpy.loadtxt() or numpy.genfromtxt() to read the data back into a NumPy array.

#writing the data text file using numpy module
# import numpy as np
# a=np.array([[1,2,3],[4,5,6],[7,8,9]])
# with open("D:\\PYTHON BACKEND\\NUMPY\\files\\aniket11.txt",'a')as fp:
#     np.savetxt(fp,a,delimiter=",")
#     print("Dat Inserted Successfully........!")


##---------------------------------------------------------------------------------
#writing the data text file using numpy module
import numpy as np
with open("D:\\PYTHON BACKEND\\NUMPY\\files\\aniket11.txt",'r')as fp:
    data=np.loadtxt(fp,delimiter=",")
    print(data)
    print("Data Read succesfully....!")

# with open("D:\\PYTHON BACKEND\\NUMPY\\files\\aniket11.txt",'r')as fp:
#     data=np.genfromtxt(fp,delimiter=",")
#     print(data)
#     print("Data Read succesfully....!")    
#---------------------------------------------------------------------------------

