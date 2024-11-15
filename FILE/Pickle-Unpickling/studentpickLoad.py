import pickle
try:
    with open("pick.data",'br')as fp:
        obj=pickle.load(fp)
        print(obj)
except FileNotFoundError:
    print("File not Found")        