# #Program for cal addition of Two Numbers by using Anonymous Functions
# #AnonymousFunEx1.py
# # def sumop(a,b):
# #     return a+b

# # addop=lambda k,v : k+v # Anonymous Function defition

# # #Main Program
# # res=sumop(10,20) # Normal Function Call
# # print("type of sumop=",type(sumop))
# # print("sum by using normal func=",res)

# # print("-----------------------------------")

# # print("Enter Two Values for addition")
# # a,b=float(input()),float(input())
# # res1=addop(a,b) # Anonymous  Function Call
# # print("Type of addop=",type(addop))
# # print("Sum by using Anonymous Function=",res1)
# #--------------------------------------------------------------------

# #Program for performing Different types of Arithmetic Operations by using Anonymous Function
# #AnonymousFunEx2.py
# from operator import floordiv


# def arithmenu():
#     print("=" * 50)
#     print("\tArithmetic Operations")
#     print("=" * 50)
#     print("\t1. Addtion")
#     print("\t2. Substration")
#     print("\t3. Multiplication")
#     print("\t4. Division")
#     print("\t5. Floor Division")
#     print("\t6. Modulo Division")
#     print("\t7. Exponentiation")
#     print("\t8. Exit")
#     print("=" * 50)
# #Anonymous Functions Definition
# addop=lambda k,v: k+v
# subop=lambda k,v: k-v
# mulop=lambda a,b: a*b
# divop=lambda k,v: k/v
# floordivop=lambda k,v: k//v
# modop=lambda k,v:k%v
# powop=lambda k,v: k**v


# #Main Program
# while(True):
#     arithmenu()
#     ch=int(input("Enter Ur Choice:"))
#     match(ch):
#         case 1:
#             print("Enter Two Values for addition")
#             a, b = float(input()), float(input())
#             res1 = addop(a, b)  # Anonymous  Function Call
#             print("\tsum({},{})={}".format(a,b,res1))
#         case 2:
#             print("Enter Two Values for Substraction")
#             a, b = float(input()), float(input())
#             res1 = subop(a, b)  # Anonymous  Function Call
#             print("\tsub({},{})={}".format(a, b, res1))
#         case 3:
#             print("Enter Two Values for Multiplication")
#             a, b = float(input()), float(input())
#             res1 = mulop(a, b)  # Anonymous  Function Call
#             print("\tmul({},{})={}".format(a, b, res1))
#         case 4:
#             print("Enter Two Values for Normal Div")
#             a, b = float(input()), float(input())
#             res1 = divop(a, b)  # Anonymous  Function Call
#             print("\tdiv({},{})={}".format(a, b, res1))
#         case 5:
#             print("Enter Two Values for Floor Div")
#             a, b = float(input()), float(input())
#             res1 = floordiv(a, b)  # Anonymous  Function Call
#             print("\tsum({},{})={}".format(a, b, res1))
#         case 6:
#             print("Enter Two Values for Mod Div")
#             a, b = float(input()), float(input())
#             res1 = modop(a, b)  # Anonymous  Function Call
#             print("\tmod({},{})={}".format(a, b, res1))
#         case 7:
#             a, b = float(input("Enter Base:")), float(input("Enter Power:"))
#             res1 = powop(a, b)  # Anonymous  Function Call
#             print("\tpow({},{})={}".format(a, b, res1))

#         case 8:
#             print("Thx for using this program")
#             break
#         case _:
#             print("Ur Selection of Operation is wrong-try again")

#  #--------------------------------------------------------------------
#  #Program for finding Biggest of Three Nums by using Anonymous Functions
# #AnonymousFunEx3.py
# findbig=lambda k,v,r:k if k>=v and k>r else v if v>k and v>=r else r if r>=k and r>v else "ALL VALUES ARE EQUAL"

# #Main Program
# print("Enter Three Numbers:")
# a,b,c=float(input()),float(input()),float(input())
# res=findbig(a,b,c) # Anonymous Function Call
# print("Big({},{},{})={}".format(a,b,c,res))

# #--------------------------------------------------------------------------

# #Program for finding Biggest of Three Nums by using Anonymous Functions
# #AnonymousFunEx4.py
# findbig=lambda k,v,r:k if v<=k>r else v if k<v>=r else r if k<=r>v else "ALL VALUES ARE EQUAL"

# #Main Program
# print("Enter Three Numbers:")
# a,b,c=float(input()),float(input()),float(input())
# res=findbig(a,b,c) # Anonymous Function Call
# print("Big({},{},{})={}".format(a,b,c,res))

# #------------------------------------------------------------------------

# #Program for finding Biggest of Multiple Nums by using Anonymous Functions
# #AnonymousFunEx5.py
# def kvrmax(lst):
#     mv=lst[0]
#     for v in lst:
#         if(v>mv):
#             mv=v
#     return mv
# def kvrmin(lst):
#     minv=lst[0]
#     for val in lst:
#         if(val<minv):
#             minv=val
#     return minv

# findmax=lambda lst: kvrmax(lst)
# findmin=lambda lst: kvrmin(lst)
# #Main Program
# print("Enter List of Values Separated by Space:")
# lst=[float(val) for val in input().split()]
# mv=findmax(lst) # Anonymous function call
# minv=findmin(lst)
# print("max({})={}".format(lst,mv))
# print("min({})={}".format(lst,minv))
#---------------------------------------------------------------------------------------------
#------------------------------------------------------------------------------------------------------

# area of circle,rectangle,square,triangle

#annyonmous function definition
# circle=lambda r:3.14*r*r
# rectangle=lambda l,b:l*b
# square=lambda s:s*s
# triangle=lambda b,h:0.5*b*h

# while(True):
#     ch=int(input("ENter a Choice: "))
#     match(ch):
#         case 1:
#             print("Enter Radius Of Circle: ")
#             r=float(input())
#             res1=circle(r)
#             print(f"Area Of Circle ={res1}")
#         case 2:
#             print("Enter Length and Breadth of the Rectangle: ")
#             l,b=float(input()),float(input())
#             res2=rectangle(l,b)
#             print(f"Area of Rectangle = {res2}")2
#         case 3:
#             print("enter a side of the square: ")
#             s=int(input())
#             res3=square(s)
#             print(f"Area of square : {res3}")
#         case 4:
#             print("Enter a base And Height:")
#             b,h=int(input()),int(input()) 
#             res4=triangle(b,h)
#             print(f"Area of Triangle ={res4}")
#         case 5:
#             print("Thnx for Using These program")  
#         case _:    
#             print("Ur Selection of Operation is wrong-try again")

#---------------------------------------------------------------------------
#different temperature conversion using annoynmous function
# 1. Celsius to Fahrenheit:
# F=( 5/9 ×C)+32
# 2.Fahrenheit to Celsius:
# C= 5/9×(F−32)  
# 3.Celsius to Kelvin:
# K=C+273.15
# 4.Kelvin to Celsius:
# C=K−273.15

# fahrenheit=lambda c:(5/9*c)+32
# celcius=lambda f:5/9 *(f-32)
# kelvin=lambda c:c+273.15
# celcius=lambda k:k-273.15

# while(True):
#     ch=int(input("Enter a choice: "))
#     match(ch):
#         case 1:
#             print("Enter temperature in celcius: ")
#             c=float(input())
#             res1=fahrenheit(c)
#             print(f"The conversion of Celsius to Fahrenheit:{res1}")
#         case 2:
#             print("Enter a temperature in Fahrenheit :")
#             f=int(input())
#             res2=celcius(f)
#             print(f"The conversion of temperture from Fahrenheit to Celsius: {res2}")
#         case 3:
#             print("Enter temperature in celcius: ")
#             c=int(input())
#             res3=kelvin(c)
#             print(f"The conversion of temperature from Celsius to Kelvin:{res3} ")
#         case 4:
#             print("Enter temperature in kelvin: ")
#             k=int (input())
#             res4=celcius(k)
#             print(f"The conversion of temperature from Kelvin to Celsius :{res4} ")     
#         case 5:
#             print("Thnx for Using These program")  
#         case _:    
#             print("Ur Selection of Operation is wrong-try again")
#----------------------------------- 

# sumtwo=lambda a,b:a if a>b else b if b>a else "TWo values are equal"

# num1=int(input("Enter a first number: "))
# num2=int(input("Enter a second number: "))
# res=sumtwo(num1,num2)
# print(res)
#---------------------------------------------------------


# variablename=lambda no of params :condition

# sumtwo=lambda a,b:a+b

# a,b=int(input("ENetr a number:")),int(input("ENetr a number:"))
# res=sumtwo(a,b)
# print(res)

#----------------------------------------------------------
#Program for Reading List of Values from KBD and Get Only +Ve Values by using Anonymous function



#Program for Reading List of Values from KBD and Get Only +Ve Values by using filter()
#Program for Reading List of Values from KBD and Get Only +Ve Values by using filter()
#Program for Reading List of Values from KBD and Get Only +Ve Values by using filter()
#Program for Accepting List of Values and get Palindrome Words by using filter
#Program for Accepting List of words and find Vowel Words


#------------------------------------

f=lambda val:val 