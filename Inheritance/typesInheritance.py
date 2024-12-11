#simple inheritance
# class A:
#     def display(self):
#         self.a=9
#         self.b=6
#         print("THese is Class A function")

# class B(A):
#     def dis(self):
#         c=self.a+self.b
#         print(f"sum={c}")

# obj = B()
# obj.display()
# obj.dis()

#multiple inheritance

# class A:
#     def first(self):
#         self.a=8
#         self.b=99
#         print("It is First Function")

# class B(A):
#     def Second(self):
#         self.c=self.a+self.b
#         print("It is Second Function")

# class C(B):
#     def Third(self):
#         print(f"sum={self.c}")
#         print("It is Third Function")

# obj=C()
# obj.first()
# obj.Second()
# obj.Third()

#mulyi level

# class A:
#     def addition(self):
#         self.a=9
#         self.b=66
#         self.c=self.a+self.b    
    
# class B:
#     def Substraction(self):
#         self.a=9
#         self.b=66
#         self.s=self.a-self.b  

# class C:
#     def div(self):
#         self.a=9
#         self.b=66
#         self.d=self.a/self.b

# class D:
#     def modulus(self):
#         self.a=7
#         self.b=8
#         self.m=self.a%self.b

# class E:
#     def mul(self):
#         self.a=8
#         self.b=99
#         self.m=self.a*self.b

# class child(A,B,C,D,E):
#     def display(self):
#         print(f"Addition={self.c}")
#         print(f"Substraction={self.s}")
#         print(f"Multiplication={self.m}")
#         print(f"Division={self.d}")
#         print(f"Modulus={self.m}")

# c =child()
# c.addition()
# c.Substraction()
# c.div()
# c.modulus()
# c.mul()
# c.display()

