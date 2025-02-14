# #read mode----bu using open()
try:
    kv=open("stude1.data",'r')
    print("file Opend in Read Mode Successfully")
except FileNotFoundError:
    print("File not Found ")

# read mode----bu using open()------by default 'r' mode is specified
# try:
#     kv=open("stude1.data")
#     print("file Opend in Read Mode Successfully")
# except FileNotFoundError:
#     print("File not Found ")    

# try:
#     kv=open("s1.data",'r')
#     print("file Opend in Read Mode Successfully")
# except FileNotFoundError:
#     print("File not Found ")
# else:
#     print("file opened siuccessfully")
# finally:
#     try:
#         print(f"is file closed={kv.closed}")
#         kv.close()
#         print(f"is file closed={kv.closed}")    
#     except NameError:
#         print("File does not Found, so no need to closed the file")    