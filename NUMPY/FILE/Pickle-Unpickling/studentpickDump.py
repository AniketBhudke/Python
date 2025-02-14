# import pickle
# def studentData():
#     with open("pick.data",'+ab')as fp:
#         studentName=input("Enter A Name Of The Student")   
#         studentSno=int(input("Enter A Student Number:"))
#         StudentMrk=float(input("Enter A Mark Of The Student: "))
#         l=list()
#         l.append(studentName)
#         l.append(studentSno)
#         l.append(StudentMrk)
#         pickle.dump(l,fp)
        
# studentData()


# class zeroLengthError(Exception):pass
# class invalidNameError(Exception):pass
# class spaceError(Exception):pass

# class nameValidation:
#     def validation(name):
#         if len(name)==0:
#             raise zeroLengthError
#         elif (not name.isalpha()):
#             raise invalidNameError
#         else:
#             words=name.split()
#             for word in words:
#                 if (not word.isspace()):
#                     print(word)
#                 else:
#                     raise spaceError   
                 


# import pickle
# class Student:
#     def pickling(self):
#         while(True):
#             try:
#                 with open("stud16.pick",'+bx')as fp:
#                     self.sno=int(input("Enter The Sudent Number:"))
#                     self.sname=nameValidation.validation(input("Enter The Student Name:"))
#                     self.smarks=float(input("Enter A Student Marks:"))
#                     l=[]
#                     l.append(self.sno)
#                     l.append(self.sname)
#                     l.append(self.smarks)
#                     pickle.dump(l,fp)
#                     print("File Successfully Load--Verify")  
#             except FileExistsError:
#                 print("File Already Exits--Try Again")
#                 break
#             except ValueError:
#                 print("Don't Enter Alnums,strs and Symbols")
#             except zeroLengthError:
#                 print("Enter the Character:")
#             except invalidNameError:
#                 print("Don't Enter Number,strs and special symbols:")
#             except spaceError:
#                 print("Your Name Contains Invalid Space:")            
#             ch=input("Do You Want To Enter Data(yes/no):")
#             if ch.lower()=="no":
#                 break  
# s = Student()
# s.pickling()

