#
# try:
#     with open("aniket.data","r") as fp:
#         filedata=fp.read()
#         print(filedata)
# except  FileNotFoundError:
#     print("File not Found")
# else:
#     print("your Data Getting Successfully...!")      

#from user input
# try:
#     filedata=input("Enter a file Name:")
#     with open(filedata,'r') as fp:
#         file=fp.read()
#         print(file)
# except FileNotFoundError:
#     print("Please Enter Correct file Name")        

#Program for Reading the Data continuously from Key Board and Write It to the File

with open("aniket.data",'a')as fp:
    filedata=input("Enter the data:")
    fp.write(filedata)
    