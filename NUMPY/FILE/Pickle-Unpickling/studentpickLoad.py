# import pickle
# try:
#     with open("pick.data",'br')as fp:
#         obj=pickle.load(fp)
#         print(obj)
# except FileNotFoundError:
#     print("File not Found")        


# import pickle
# class Student:
#     def unpickling(self):
#         while(True):
#             try:
#                 filedata=input("Enter The File Name That Contain .pick Extension:")
#                 with open(filedata,'rb')as fp:
#                     var=pickle.load(fp)
#                     print(var)
#                     print("FIle Read Successfully--Verify")
#             except FileNotFoundError:
#                 print("File Not Found ---Try Again")  
#             except ValueError:
#                 print("Don't Enter Alnums,Stars and Symbols")    
#             ch=input("Do You Want to see again Data(yes/no)")
#             if ch.lower()=="no":
#                 break          
# s = Student()
# s.unpickling()    
    

