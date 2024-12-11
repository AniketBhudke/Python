# class employee:
#     @classmethod
#     def getvalues(cls):
#         cls.compname="IBM"
#         cls.city="HYD"


#     def displayvalues(cls):
#         print(f"comapny Name={cls.compname}")
#         print(f"City ={cls.city}")    

# eo = employee()
# eo.getvalues()
# eo.displayvalues()
# print("-------------------------")
# print(employee.city)
# print(employee.compname)

# class employee:
#     @classmethod
#     def getEmp(cls):
#         cls.comp=input("Enter The company Name:")
#         cls.city=input("Enter The City oF the Student:")
#     @classmethod    
#     def displayEmp(cls):
#         print(f"The Company name:{cls.comp}")
#         print(f"the city of employee:{cls.city}")

#     def getdaat(self):
#         self.comp=input("Enter The Company Name:")
#         self.city=input("Enter the city :")
#     def displayData(self):
#         print(f"The Company name:{self.comp}")
#         print(f"the city of employee:{self.city}")

# eo =employee()
# eo.getEmp()
# eo.displayEmp()
# eo.getdaat()
# eo.displayData()

class Emp:
    def getempvals(self):
        self.eno=int(input("Enter Employee Number:"))
        self.name = input("Enter Employee Name:")
        self.sal=float(input("Enter Employee Salary:"))

class Student:
    def getstudvals(self):
        self.sno = int(input("Enter Student Number:"))
        self.name = input("Enter Student Name:")

class Teacher:
    def getteachervals(self):
        self.tno=int(input("Enter Teacher Number:"))
        self.name = input("Enter Teacher Name:")
        self.exp=float(input("Enter Teacher Exp:"))
        self.subject=input("Enter Teacher Subject:")
class HYD:
    @staticmethod
    def dispobjectdata(obj,objinfo):
        print("---------------------------------")
        print("{} Object Information".format(objinfo))
        print("---------------------------------")
        for dmn,dmv in obj.__dict__.items():
            print("\t{}--->{}".format(dmn,dmv))
        print("---------------------------------")


#Main Program
e=Emp()
s=Student()
t=Teacher()
e.getempvals()
print("-----------------------------------------")
s.getstudvals()
print("-----------------------------------------")
t.getteachervals()
print("-----------------------------------------")
# we are taking static method which will display
# the content of any object of any class
HYD.dispobjectdata(e,"Employee") # Calling Static Method w.r.t Class Name
HYD.dispobjectdata(s,"Student") # Calling Static Method w.r.t Class Name
HYD.dispobjectdata(t,"Teacher") # Calling Static Method w.r.t Class NameE 