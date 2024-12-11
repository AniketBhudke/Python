# class Account:
#     def details(self):
#         self.__name="aniket"
#         self.accountNo=8
#         self.bname="SBI"
#         self.aType="saving"
#         print(f"Acoount Number={self.accountNo}")
#         print(f"Account Branch Name:{self.bname}")
#         print(f"Account Type={self.aType}")
#         # print(f"Acount Holder Name={self.name}")#it gives attribute erroe

# a = Account()
# a.details()

# class Account:
#     def __details(self):
#         self.name="aniket"
#         self.accountNo=8
#         self.bname="SBI"
#         self.aType="saving"
#         print(f"Acoount Number={self.accountNo}")
#         print(f"Account Branch Name:{self.bname}")
#         print(f"Account Type={self.aType}")
#         # print(f"Acount Holder Name={self.name}")#it gives attribute erroe

# a = Account()
# a.details()#it gives attributeError


# class __Account:
#     def details(self):
#         self.name="aniket"
#         self.accountNo=8
#         self.bname="SBI"
#         self.aType="saving"
#         print(f"Acoount Number={self.accountNo}")
#         print(f"Account Branch Name:{self.bname}")
#         print(f"Account Type={self.aType}")
#         print(f"Acount Holder Name={self.name}")#it gives attribute erroe

# a = Account()#NameError
# a.details()


# class Account:
#     def ____init__(self):
#         self.__name="aniket"
#         self.accountNo=8
#         self.bname="SBI"
#         self.aType="saving"
#         print(f"Acoount Number={self.accountNo}")
#         print(f"Account Branch Name:{self.bname}")
#         print(f"Account Type={self.aType}")
#         # print(f"Acount Holder Name={self.name}")#it gives attribute erroe

# a = Account()#does not run the program


class Account:
    def details(self):
        self.__name="aniket"
        self.accountNo=8
        self.bname="SBI"
        self.aType="saving"
        print(f"Acoount Number={self.accountNo}")
        print(f"Account Branch Name:{self.bname}")
        print(f"Account Type={self.aType}")
        print(f"Acount Holder Name={self.__name}")

a = Account()
a.details()


