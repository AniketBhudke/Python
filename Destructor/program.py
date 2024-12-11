# import time
# class Student:
#     def __init__(self):
#         self.sname="ANiket"
#         self.sno=6

#     def __del__(self):
#         print("GC Calls __del__() for de-allocating the memory space of current object:{}".format(id(self)))

# s = Student()
# s1 = Student()
# s2 = Student()
# time.sleep(1)

# import sys
# class Employee:
#     def __init__(self,eno,ename):
#         print(f"I am from parametrized constructor--object ID:{id(self)}")
#         self.eno=eno
#         self.ename=ename
#         print(f"EMP number:{self.eno}")
#         print(f"EMP Name:{self.ename}")

#     def __del__(self):
#         global memspace
#         print(f"GC Calls __del__() for de-allocating the memory space of currnt object:{id(self)}")    
#         memspace=memspace-sys.getsizeof(self)#getssizeof() is a function that get the how many amount of size your object can take
#         print("Now Memory Space=",memspace)

# e1 = Employee(10,"RS")
# e2 = Employee(10,"RS")
# e3 = Employee(10,"RS")
# memspace=sys.getsizeof(e1)+sys.getsizeof(e2)+sys.getsizeof(e3)

# class Student:
#     def __init__(self,eno,ename):
#         self.eno=eno
#         self.ename=ename
#         print(f"value of eno={self.eno}\n name of student ={self.ename}")
#     def __del__(self):
#         print(f"We can destroy the object of ID:{id(self)}")

# s=Student(22,"ts")
# s1=s
# s2=s

# s1=Student(2,"s")
# s3=Student(222,"aniket")
# a=4
# b=a
# print(id(a),id(b))


import time,sys,gc
class Employee:
	def __init__(self,eno,ename):
		print("I am from Parametrized Constructor-Object ID:{}".format(id(self)))
		self.eno=eno
		self.ename=ename
		print("\tEmp Number:{}".format(self.eno))
		print("\tEmp Name:{}".format(self.ename))
		print("--------------------------------------------------")
	def  __del__(self):
		global memspace
		print("GC Calls __del__() for de-allocating the memory space of current object:{}".format(id(self)))
		memspace=memspace-sys.getsizeof(self)
		print("\tNow Memory space=",memspace)

#Main Program
print("Program Execution Started")
print("Initially, is GC Running=",gc.isenabled())
print("--------------------------------------------------")
e1=Employee(10,"RS") # Object Creation--makes the PVM to call Parametrized Constructor
e2=Employee(20,"TR") # Object Creation--makes the PVM to call Parametrized Constructor
e3=Employee(30,"JH") # Object Creation--makes the PVM to call Parametrized Constructor
#calculate memory space objects of current object
memspace=sys.getsizeof(e1)+sys.getsizeof(e2)+sys.getsizeof(e3)
print("Total Memory space of all objects=",memspace)
gc.disable()
print("Program Execution Ended")
print("Now is GC Running=",gc.isenabled())
print("--------------------------------------------------")
time.sleep(10)