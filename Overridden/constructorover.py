# class c1:
#     def __init__(self):
#         print("It is C1 class constructor")

# class c2(c1):
#     def __init__(self):
#         print("It Is C2 class Constructor")

# class c3(c2):
#     def __init__(self):
#         print("It Is C3 class Constructor")

# c=c3()

# class c1:
#     def __init__(self):
#         print("It is C1 class constructor")

# class c2():
#     def __init__(self):
#         print("It Is C2 class Constructor")

# class c3(c2,c1):
#     def __init__(self):
#         print("It Is C3 class Constructor")
#         super().__init__()
#         c1.__init__(self)

# c=c3()


from math import pi
class Circle:
    def __init__(self, r):  # Original Constructor
        self.ac = pi * r ** 2
        print("Area of Circle={}".format(round(self.ac, 2)))
class Square(Circle):
    def __init__(self, s):  # Overriden Constructor
        self.sa = s ** 2
        print("Area of Square={}".format(self.sa))
class Rect(Square):

    def area(self, L, B):  # Method Name
        self.ar = L * B
        print("Area of Rect={}".format(self.ar))
        print("--------------------------------")
        super().__init__(float(input("Enter Side Value of Square:")))
        print("--------------------------------")
        Circle.__init__(self,float(input("Enter Radius:")))
#main Program
r = Rect() # Object Creation--PVM Calls Default Cont of Rect Class
L = float(input("Enter Length:"))
B = float(input("Enter Breadth:"))
r.area(L,B)


# from math import pi
# class Circle:
#     def __init__(self, r):  # Original Constructor
#         self.ac = pi * r ** 2
#         print("Area of Circle={}".format(round(self.ac, 2)))
# class Square(Circle):
#     def __init__(self, s):  # Overriden Constructor
#         self.sa = s ** 2
#         print("Area of Square={}".format(self.sa))
# class Rect(Square):
#     def __init__(self):
#         print("--------------------------------")
#         super().__init__(float(input("Enter Side Value of Square:")))
#         print("--------------------------------")
#         Circle.__init__(self, float(input("Enter Radius:")))
#         print("--------------------------------")
#     def area(self, L, B):  # Method Name
#         self.ar = L * B
#         print("Area of Rect={}".format(self.ar))
#         print("--------------------------------")

# #main Program
# r = Rect() # Object Creation--PVM Calls Default Cont of Rect Class
# L = float(input("Enter Length:"))
# B = float(input("Enter Breadth:"))
# r.area(L,B)