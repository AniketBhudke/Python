# #read mode----bu using open()
# try:
#     kv=open("stude1.data",'r')
#     print("file Opend in Read Mode Successfully")
# except FileNotFoundError:
#     print("File not Found ")
#----------------------------------------------------------------------------
#read mode----bu using open()------by default 'r' mode is specified
# try:
#     kv=open("stude1.data")
#     print("file Opend in Read Mode Successfully")
# except FileNotFoundError:
#     print("File not Found ")    
#-----------------------------------------------------------------------
# try:
#     kv=open("s.data",'r')
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
#---------------------------------------------------------------------------------------
# kv=open("s.data",'w')
# print("file craeted successfully opened in nwrite mode")
#-------------------------------------------------------------------------
#write mode---by using with open() as w-----write
# with open("stud.data",'w') as fp:
#     print(fp)
#     print("File created Successsfully..!")
#     print(f"Mode of the Files ={fp.mode}")
#     print(f"Name of the Files ={fp.name}")
#     print(f"Is file open in Writable={fp.writable()}")
#     print(f"Is file open in Readable={fp.readable()}")
#-----------------------------------------------------------------------
#append mode----by using with open() as ---a---write
# with open("std.data",'a') as fp:
#     print("File created Successsfully..!")
#     print(f"Mode of the Files ={fp.mode}")
#     print(f"Name of the Files ={fp.name}")
#     print(f"Is file open in Writable={fp.writable()}")
#     print(f"Is file open in Rritable={fp.readable()}")
#-----------------------------------------------------------------------
#read mode----by using with open() as ---+r----read and write
# with open("std.data",'+r') as fp:
#     print("File created Successsfully..!")
#     print(f"Mode of the Files ={fp.mode}")
#     print(f"Name of the Files ={fp.name}")
#     print(f"Is file open in Writable={fp.writable()}")
#     print(f"Is file open in Rritable={fp.readable()}")
#-----------------------------------------------------------------------
#write mode----by using with open() as ---+w-----write and read
# with open("std.data",'+w') as fp:
#     print("File created Successsfully..!")
#     print(f"Mode of the Files ={fp.mode}")
#     print(f"Name of the Files ={fp.name}")
#     print(f"Is file open in Writable={fp.writable()}")
#     print(f"Is file open in Rritable={fp.readable()}")
#-----------------------------------------------------------------------
#x mode----by using with open() as ---x----write only
# try:
#     with open("sd1.data",'x') as fp:
#         print("File created Successsfully..!")
#         print(f"Mode of the Files ={fp.mode}")
#         print(f"Name of the Files ={fp.name}")
#         print(f"Is file open in Writable={fp.writable()}")
#         print(f"Is file open in Rritable={fp.readable()}")
# except FileExistsError:
#     print("File Already Created")
#-----------------------------------------------------------------------------
#x+ mode----by using with open() as ---x+------write and read
# try:
#     with open("std2.data",'x+') as fp:
#         print("File created Successsfully..!")
#         print(f"Mode of the Files ={fp.mode}")
#         print(f"Name of the Files ={fp.name}")
#         print(f"Is file open in Writable={fp.writable()}")
#         print(f"Is file open in Rritable={fp.readable()}")
# except FileExistsError:
#     print("File Already Created")
#-------------------------------------------------------------------------------