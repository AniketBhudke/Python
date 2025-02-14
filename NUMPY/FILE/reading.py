#
try:
    with open("A1.data","+a") as fp:
        # fp.seek(4)
        # filedata=fp.readline(10)
        fp.seek(0)
        filedata=fp.readline()
        print(filedata)
except  FileNotFoundError:
    print("File not Found")
else:
    print("your Data Getting Successfully...!")      

#from user input
# try:
#     filedata=input("Enter a file Name:")
#     with open(filedata,'r') as fp:
#         file=fp.read()
#         print(file)
# except FileNotFoundError:
#     print("Please Enter Correct file Name")        

#Program for Reading the Data continuously from Key Board and Write It to the File

# with open("reading.py",'a')as fp:
#     filedata=input("Enter the data:")
#     fp.tell(10)
#     fp.write(filedata)
    