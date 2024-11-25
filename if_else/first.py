# # #Program for accepting any digit and display Its Name
# # d1={1:"one",2:"two",3:"three",4:"four",5:"five",6:"six",7:"seven",8:"eight",9:"nine",0:"zero"}
# # digit=int(input("enter any digit:"))
# # # result= d1.get(digit) if  d1.get(digit)!=None else "+ve number" if digit>9 else "-ve number" if digit  in [-1,-2,-3,-4,-5,-6,-7,-8,-9] else "-ve"
# # # print("{} is {}".format(digit,result))


# # if d1.get(digit)!=None:
# #     print(d1.get(digit))
# # elif digit>9:
# #     print("it is positive digit")
# # elif digit in [-1,-2,-3,-4,-5,-6,-7,-8,-9]:
# #     print("it is -ve number")
# # else:
# #     print("it is -ve digit")            


# # a=float(input("Enter First Value:"))
# # b=float(input("Enter Second Value:"))
# # if(a>b):
# #     print("max({},{})={}".format(a,b,a))
# # else:
# #     if(b>a):
# #         print("Max({},{})={}".format(a,b,b))
# #     else:
# #         print("Both the Values are equal")
# #     print("I am from if..else--inner")
# # print("I am from if..else--outer")


# # # Program for Deciding the word whether It is Vowel or not
# # word=input("enter a string:").lower()
# # if ('a' in word) or ('e' in word) or ('i' in word) or ('o' in word) or ('u' in word):
# #     print("it is vowel")
# # else:
# #     print("it is not vowel")    

# # a=float(input("Enter Value of a:"))
# # b=float(input("Enter Value of b:"))
# # c=float(input("Enter Value of c:"))
# # bigv=a if b<=a>c else b if a<b>=c else c if a<=c>b else "All Values are equal"
# # print("Big({},{},{})={}".format(a,b,c,bigv))

# s=["python"]
# s1=["programming"]
# x= "   ".join(s1)
# print(x)q q


# print("Bhrat")




# ch=int(input("Enter Ur Choice:"))
# match(ch):
#     case 1:
#         F=float(input("Enter the Temp in terms of F:"))
#         C = (F - 32)*(5 / 9)
#         print("Given Temp in F:{}".format(F))
#         print("Eqv Temp in C:{}".format(C))
#     case 2:
#         F = float(input("Enter the Temp in terms of F:"))
#         K=(F - 32)*(5 / 9) + 273.15
#         print("Given Temp in F:{}".format(F))
#         print("Eqv Temp in K:{}".format(K))
#     case 3:
#         C = float(input("Enter the Temp in terms of C:"))
#         F = C*(9 / 5) + 32
#         print("Given Temp in C:{}".format(C))
#         print("Eqv Temp in F:{}".format(F))
#     case 4:
#         C = float(input("Enter the Temp in terms of C:"))
#         K=C + 273.15
#         print("Given Temp in C:{}".format(C))
#         print("Eqv Temp in K:{}".format(K))
#     case 5:
#         K = float(input("Enter the Temp in terms of K:"))
#         F = (K-273.15)*(9/5) + 32
#         print("Given Temp in K:{}".format(K))
#         print("Eqv Temp in F:{}".format(F))
#     case 6:
#         K = float(input("Enter the Temp in terms of K:"))
#         C=K - 273.15
#         print("Given Temp in K:{}".format(K))
#         print("Eqv Temp in C:{}".format(round(C,2)))
#     case _:
#         print("Thx for Using Program")






# ch=input("Enter Ur Choice:")
# match(ch):
#     case "R"|'r':
#         L,B=float(input("Enter Length:")),float(input("Enter Breadth:"))
#         ar=L*B
#         print("Area of Rect={}".format(ar))
#     case "T"|'t':
#         B, H = float(input("Enter Base:")), float(input("Enter Height:"))
#         at=(1/2)*B*H
#         print("Area of Triangle:{}".format(at))
#         print("--------------OR--------------------------")
#         a,b,c=float(input("Enter Side1:")),float(input("Enter Side2:")),float(input("Enter Side3:"))
#         s=(a+b+c)/2
#         ats=(s*(s-a)*(s-b)*(s-c))**0.5
#         print("Area of Triangle:{}".format(ats))
#     case "S"|'s':
#         s1 = float(input("Enter Side:"))
#         sa = s1*s1
#         print("Area of Square={}".format(sa))
#     case "C"|'c':
#         r = float(input("Enter Radius:"))
#         ca = 3.14*r**2
#         print("Area of Square={}".format(ca))
#     case "E"|'e':
#         print("thx for using Program")
#         sys.exit()
#     case _:
#         print("Ur Selection of Operation is Wrong--try again")

s="python         "
s=s.rstrip()
print(s)
