# #str
# var="python"
# print(var[4:0])
# print(var[:1:-1])

# sqr=lambda a,b:a+b
# print(sqr(3,4))

# class a:
#     def ab(self,a,b):
#         print(a+b)
#     def cd(self,c,d):
#         print(c-d)

# d=a()
# d.ab(44,55)
# d.cd(5,6)

class a:
    def __init__(self,name):
        self.name=name
        print(name)
    def __del__(self):
        print('Destructor called')  
        a=5
        print("f")  
p1 = a("aniket")        
del p1

        