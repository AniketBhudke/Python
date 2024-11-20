try:
    with open("aniket.data","r") as fp:
        filedata=fp.read()
        print(filedata)
except  FileNotFoundError:
    print("File not Found")
else:
    print("your Data Getting Successfully...!")      
