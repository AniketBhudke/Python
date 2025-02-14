import os
try:
    os.mkdir("D:\\PYTHON BACKEND\\OsFiles\\Practice31")
except FileExistsError:
    print("File Already Exist")
except FileNotFoundError:
    print("Root Folder Not Found Error")

