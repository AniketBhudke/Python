# class InvalidNumberError(Exception):pass
# class zeroLengthError(Exception):pass
# class spaceNameError(Exception):pass
# import oracledb as orc

# class nameValidation:
#     def Validation(self,name):
#         if len(name)==0:
#             raise zeroLengthError
#         elif (name.isspace()):
#             raise spaceNameError
#         else:
#             res=True
#             words=name.split()
#             for word in words:
#                 if not(word.isalpha()):
#                     res=False
#             if(res):
#                 return name
#             else:
#                 raise InvalidNumberError
# #------------------------------------------------------------------------------------------

# class Student:
#     def getdata(self):
#         try:
#             self.sno=int(input("Enter A Student number:"))
#             self.sname=nameValidation().Validation(input("Enter a Student Name:" ))
#             self.smarks=int(input("Enter A student Marks:"))   
#         except InvalidNumberError:
#             print("Enter Ur Name: ")
#         except zeroLengthError:
#             print("Enter The Charcter:")
#         except spaceNameError:
#             print("Don't Enter The Space")                
#         else:
#             self.displaystudData()  

#     def displaystudData(self):
#         print(f"Student Number={self.sno}")
#         print(f"Student Name:{self.sname}")
#         print(f"Student Marks={self.smarks}")
#         self.savestudData()

#     def savestudData(self):
#         try:
#             conn=orc.connect("ANIKET/1234@localhost/orcl")
#             cur=conn.cursor()
#             iq="insert into STUDENT(SNO,SNAME,SMARKS) values(%d,'%s',%d)"
#             cur.execute(iq %(self.sno,self.sname,self.smarks))
#             conn.commit()
#             print("Data Inserted Successfully--Verify")
#         except orc.DatabaseError as db:
#             print(f"Problem in Oracle DB:{db}")
# s=Student()
# s.getdata()

# outer_list=[]
# values=int(input("How Many Value You Want:"))
# for i in range(values):
#         val=int(input("Enter The value:"))
#         outer_list.append(val)
# print(outer_list)        

# class Student:
#         def info(self):
#                 self.sno=int(input("Enter The Student Number:"))
#                 self.Sname=input("Enter The Student name:")
#                 self.SMarks=int(input("Enter The Student MArks:"))

#         @staticmethod
#         def displayData(s):
#                 print(f"Student Number:{s.sno}")
#                 print(f"Student Name={s.Sname}")
#                 print(f"Student Marks={s.SMarks}")

# s = Student()
# s.info()
# s.displayData(s)
