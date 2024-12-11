class Student:
    def __init__(self):
        print("It Is default Constructor:")

s = Student()

class Student:
    def __init__(self,a,b):
        print("It Is Parametrized Constructor:")
        self.k=a
        self.v=b
        print(f"a={self.k} and b={self.v}")

s = Student(10,5)


# class Student:
#     def __init__(self,name="Aniket",percentage="56%"):
#         print(f"It Is Parametrized And Default COnstructor:")
#         self.n=name
#         self.p=percentage
#         print(f"Name={self.n} \t Percentage={self.p}")

# s = Student()   
# s1=Student("harshal",78)     

# class unique_Element:
#     def __init__(self):
#         lst=[]
#         size=int(input("How Many Value You Want Insert in The List:"))
#         for i in range(size):
#             value=input("Enter The Value Of the List:")
#             if value.isdigit():
#                 value = int(value)
#             lst.append(value)
#         lst1=[]
#         for val in lst:
#             if  val not in lst1:
#                 lst1.append(val)
#         print(lst1) 

# s = unique_Element()

#5
#5*4*3*2*1

# class factorial:
#     def __init__(self):
#         lst=[]
#         size=int(input("How Many Value You Want Insert in The List:"))
#         for i in range(size):
#             value=int(input("Enter The Value Of the List:"))
#             lst.append(value)
#         for value in lst:
#             lst_fact=[]
#             fact=1
#             for i in range(1,value):
#                 fact=fact*i
#                 lst_fact.append(fact)
#         print(lst_fact)

# fac =factorial()


        



    

