
# def ReadData():
#     while(True):
#             try:
#                 with open("A1.data","w")as wr:
#                     sno=int(input("Enter A student Number:"))
#                     sName=input("Enter A Student Name:")
#                     sMarks=int(input("Enter A Student Marks:"))
#                     wr.write(str(sno))
#                     wr.write(sName)
#                     wr.write(str(sMarks))
#                     wr.seek(0)
#             except FileNotFoundError:
#                 print("File Already Exists--Verify")    
#             ch=input("Do You Want Write The Data In File--(Yes/No)")
#             if ch.lower()=="no":
#                 print("Data in the File Successfully -- Verify")  
#                 break
# ReadData()

# def WriteData():
#     try:
#         with open("A.data",'r')as wr:
#             rd=wr.read()
#             wr.seek(0)
#         print(rd)
#     except FileNotFoundError:
#         print("File Not Found--Try Again")
#     ch=input("Do You Want To Read Data Again-(yes/no)")
#     if ch.lower()=="no":
#         print("Data SuccessFully Raed--Verify")

# WriteData()
