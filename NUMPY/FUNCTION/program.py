# Approach1:funtion with return type with parameter
# --------------------------------------------------
# #INPUT          : Taking from Function Call
# #PROCESS   : Done inside of Function Body
# #RESULT      : Giving Back to Function Call
# --------------------------------------------------
# def addop(a,b):
#     c=a+b
#     return c

# x=float(input("Enter First Value:"))
# y=float(input("Enter Second Value:"))
# z=addop(x,y) # function call
# print(f"sum({x}{y})={z}")
 

# Approach2:function with no return type and no parameter
# --------------------------------------------------
# #INPUT     : Inside the Function Body
# #PROCESS   : Inside the Function Body
# #RESULT    : Inside the Function Body
# --------------------------------------------------

# def addop():
#     a=float(input("Enter First Value:"))
#     b = float(input("Enter Second Value:"))
#     #Processing
#     c=a+b
#     #Display the Result
#     print(f"sum({a}{b})={c}")

# #Main Program
# addop() # Function Call

# Approach3:function  no return type and with parameter
# --------------------------------------------------
# #INPUT     : Taking from Function Call
# #PROCESS   : Done inside of Function Body
# #RESULT    : Inside the Function Body
# --------------------------------------------------
# def addop(a,b):
#     c=a+b
#     print("sum({},{})={}".format(a,b,c))

# #Main Program
# x=float(input("Enter First Value:"))
# y=float(input("Enter Second Value:"))
# addop(x,y) # Function Call


# Approach4:function with no parameter and with return type
# --------------------------------------------------
# #INPUT     : Inside the Function Body
# #PROCESS   : Inside the Function Body
# #RESULT    : Giving Back to Function Call
# ------------------------------------
# def addop():
#     # Take the Input
#     a = float(input("Enter First Value:"))
#     b = float(input("Enter Second Value:"))
#     # Processing
#     c = a + b
#     #Give the Result Back to Function Call
#     return a,b,c # here return not returns Single Value But also returns More than one value
# #Main Program
# a,b,c=addop() # Function Call with Multi Line assigment
# print("sum({},{})={}".format(a,b,c))
# print("---------------OR---------------------")
# res=addop() # Function Call with Single Line assigment
# #here res is an object of <class, tuple>
# print("sum({},{})={}".format(res[0],res[1],res[2]))
# print("-----------OR----------------")
# print("sum({},{})={}".format(res[-3],res[-2],res[-1]))

#------------------------------------------------------------------------------------------------------------
#calculate simple intersted and total amount to pay
# si=p*r*t
# total=si+p
#----------------------------------------------------------------------------------------------------------------

#approach 1:function with return type and with parameter
#-----------------------------------
# def simpleintersted(p,r,t):
#     si=p*r*t
#     total=si+p
#     return si,total

# p=int(input("Enter a principal Amount: "))
# r=int(input("Enter a rate of intersted : "))
# t=int(input("Enter a time : "))
# si,total=simpleintersted(p,r,t)
# print(f"{p}*{r}*{t}={si}")
# print(f"{si} + {p}= {total}")

#approach 2:function with no return type and with no  parameter
#-----------------------------------------------
# def simpleintersted():
#     p=int(input("Enter a principal Amount: "))
#     r=int(input("Enter a rate of intersted : "))
#     t=int(input("Enter a time : "))
#     si=p*r*t
#     print(f"{p}*{r}*{t}={si}")
#     total=si+p
#     print(f"{si} + {p}= {total}")

# simpleintersted()

#approach 3:function with  no return type and with  parameter
#--------------------------------------------------
# def simpleintersted(p,r,t):
#     si=p*r*t
#     print(f"{p}*{r}*{t}={si}")
#     total=si+p
#     print(f"{si} + {p}= {total}")

# p=int(input("Enter a principal Amount: "))
# r=int(input("Enter a rate of intersted : "))
# t=int(input("Enter a time : "))

# simpleintersted(p,r,t)
    
#approach 4:function with  return type and with no  parameter
#--------------------------------------------
# def simpleintersted():
#     p=int(input("Enter a principal Amount: "))
#     r=int(input("Enter a rate of intersted : "))
#     t=int(input("Enter a time : "))
#     si=p*r*t
#     total=si+p
#     return p,r,t,si,total

# res=simpleintersted()
# print(f"{res[0]}*{res[1]}*{res[2]}={res[3]}")
# print(f"{res[3]} + {res[0]}= {res[-1]}")

#----------------------------------------
#area of rectangle
# area=length*breadth
#-------------------------------------------

#approach 1:function with return type and with parameter
#-----------------------------------
# def rect(l,b):
#     area=l*b
#     return area

# length=int(input("Enter a length of reactangle: "))
# breadth=int(input("Enter a breadth of reactangle: "))
# area=rect(length,breadth)
# print(f"{length}*{breadth}={area}")

#approach 2:function with no return type and with no  parameter
#-----------------------------------------------
# def rect():
#     l=int(input("Enter a length of reactangle: "))
#     b=int(input("Enter a breadth of reactangle: "))
#     area=l*b
#     print(f"{l}*{b}={area}")

# rect()    

#approach 3:function with  no return type and with  parameter
#--------------------------------------------------
# def rect(l,b):
#     area=l*b
#     print(f"{l}*{b}={area}")

# l=int(input("Enter a length of reactangle: "))
# b=int(input("Enter a breadth of reactangle: "))     
# rect(l,b)

#approach 4:function with  return type and with no  parameter
#--------------------------------------------
# def rect():
#     l=int(input("Enter a length of reactangle: "))
#     b=int(input("Enter a breadth of reactangle: "))
#     area=l*b
#     return l,b,area

# res=rect()
# print(f"{res[0]}*{res[1]}={res[-1]}")     

#------------------------------------------------------------------------------------------------------------------------
#area of circle
# area=3.14*r*r
#---------------------------------------------------------------------------------------------------------------------------

#approach 1:function with return type and with parameter
#-----------------------------------
# def circle(r):
#     area=3.14*r*r
#     return area

# radius=int(input("enter aradius:"))
# a=circle(radius)
# print(f"3.14 * {radius} * {radius}={a}")

#approach 2:function with no return type and with no  parameter
#-----------------------------------------------
# def circle():
#     r=int(input("enter aradius:"))
#     area=3.14*r*r
#     print(f"3.14 * {r} * {r}={area}")

# circle()    

#approach 3:function with  no return type and with  parameter
#--------------------------------------------------
# def circle(r):
#     area=3.14*r*r
#     print(f"3.14 * {r} * {r}={area}")

# radius=int(input("enter aradius:"))
# circle(radius)

#approach 4:function with  return type and with no  parameter
#--------------------------------------------
# def circle():
#     r=int(input("enter aradius:"))
#     area=3.14*r*r
#     return r,area

# res=circle()
# print(f"3.14 * {res[0]}* {res[0]}=  {res[-1]}")


#-----------------------------------------------------------------------------------------------------------------------
#area and perimeter of square
# area=side*side
# perimeter=4*side
#------------------------------------------------------------------------------------------------------------------------

#approach 1:function with return type and with parameter
#-----------------------------------
# def area_square(side):
#     area=side*side
#     return area

# def perimeter_square(side):
#     perimeter=4*side
#     return perimeter

# s=int(input("Enter a side of square: "))

# a=area_square(s)
# print(f"{s} * {s} = {a}")

# p=perimeter_square(s)
# print(f"{s} * 4 = {p}")


#approach 2:function with no return type and with no  parameter
#-----------------------------------------------
# def area_square():
#     side=int(input("enter a side of square: "))
#     area=side*side
#     print(f"{side} * {side} = {area}")

# def perimeter_square():
#     side=int(input("enter a side of square: "))
#     perimeter=4*side
#     print(f"{side} * 4 = {perimeter}")
# area_square()
# perimeter_square()


#approach 3:function with  no return type and with  parameter
#--------------------------------------------------
# def area_square(side):
#     area=side*side
#     print(f"{side}* {side}={area}")

# def perimeter_square(side):
#     perimeter=4*side
#     print(f"{side}* 4 ={perimeter}")

# s=int(input("enter a side of square:"))

# area_square(s)

# perimeter_square(s)

#approach 4:function with  return type and with no  parameter
#--------------------------------------------

# def area_square():
#     s=int(input("enter a side of square:"))
#     area=s*s
#     return area,s 

# def perimeter_square():
#     s=int(input("enter a side of square:"))
#     perimeter=4*s
#     return perimeter,s

# a,b=area_square()
# print(f"{b} * {b} = {a}")
# print("------------------------OR--------------------------------------")
# res=area_square()
# print(f"{res[1]} * {res[1]} = {res[0]}")
# print("------------------------OR--------------------------------------")

# res=perimeter_square()
# print(f"{res[1]} * {res[1]} = {res[0]} ")


#-----------------------------------------------------------------------------------------------------------------------
#area and perimeter of triangle
# area=1\2 *base *height
# perimeter=length + length + length
#------------------------------------------------------------------------------------------------------------------------

#approach 1:function with return type and with parameter
#-----------------------------------
# def area_triangle(b,h):
#     area=0.5 *b *h
#     return area

# def perimeter_triangle(l1,l2,l3):
#     perimeter=l1 + l2 + l3
#     return perimeter

# base=int(input("enter a Base : "))
# height=int(input("enter a height: "))
# a=area_triangle(base,height)
# print(f"area of triangle={a}")

# length1=int(input("Enter a length of first Side:"))
# length2=int(input("Enter a length of second Side:"))
# length3=int(input("Enter a length of third Side:"))
# p=perimeter_triangle(length1,length2,length3)
# print(f"Perimeter of Triangle={p}")

#approach 2:function with no return type and with no  parameter
#-----------------------------------------------
# def area_triangle():
#     base=int(input("enter a Base : "))
#     height=int(input("enter a height: "))
#     area=0.5 *base *height
#     print(f"area of triangle={area}")
# area_triangle()  

# def perimeter_triangle():
#     length1=int(input("Enter a length of first Side:"))
#     length2=int(input("Enter a length of second Side:"))
#     length3=int(input("Enter a length of third Side:"))
#     perimeter=length1 + length2 + length3
#     print(f"Perimeter of Triangle={perimeter}")
# perimeter_triangle()

#approach 3:function with  no return type and with  parameter
#--------------------------------------------------
# def area_triangle(b,h):
#     area=0.5 *b *h
#     print(f"area of triangle={area}")

# def perimeter_triangle(length1,length2,length3):
#     perimeter=length1 + length2 + length3
#     print(f"Perimeter of Triangle={perimeter}")


# base=int(input("enter a Base : "))
# height=int(input("enter a height: "))  
# area_triangle(base,height)

# l1=int(input("Enter a length of first Side:"))
# l2=int(input("Enter a length of second Side:"))
# l3=int(input("Enter a length of third Side:"))
# perimeter_triangle(l1,l2,l3)    

#approach 4:function with  return type and with no  parameter
#--------------------------------------------
# def area_triangle():
#     b=int(input("enter a Base : "))
#     h=int(input("enter a height: "))  
#     area=0.5 *b *h  
#     return area

# def perimeter_triangle():
#     l1=int(input("Enter a length of first Side:"))
#     l2=int(input("Enter a length of second Side:"))
#     l3=int(input("Enter a length of third Side:"))
#     perimeter=l1 + l2 + l3
#     return perimeter

# a=area_triangle()
# print(f"Area of triangle ={a}")

# p=perimeter_triangle()
# print(f"Perimeter of triangle ={p}")

#-----------------------------------------------------------
#accept word and decide whether it is palindrome or not
#-----------------------------------------------------------------
#approach 1:function with return type and with parameter
#-----------------------------------
# def palindrome(w):
#     if w == w[::-1]:
#         return "it is palindrome"
#     else:
#         return "it is not palindrome"

# word=input("Enter a string: ")
# a=palindrome(word)
# print(a)

#approach 2:function with no return type and with no  parameter
#-----------------------------------------------

# def palindrome():
#     w=input("Enter a string: ")
#     if w == w[::-1]:
#         print( "it is palindrome")
#     else:
#         print("it is not palindrome")

# palindrome()    

#approach 3:function with  no return type and with  parameter
#--------------------------------------------------

# def palindrome(w):
#     if w == w[::-1]:
#         print("it is palindrome")
#     else:
#         print("it is not palindrome")

# word=input("Enter a string: ")
# palindrome(word)

#approach 4:function with  return type and with no  parameter
#--------------------------------------------

# def palindrome():
#     w=input("Enter a string: ")
#     if w == w[::-1]:
#          return "it is palindrome"
#     else:
#         return "it is not palindrome"

# res=palindrome()
# print(res)



#--------------------------------------------------------------------------------------
#area of rectangle
# area=length*breadth
#-----------------------------------------------------------------------------

#approach 1:function with return type and with parameter
#-----------------------------------
# def rect(l,b):   
#   area=l*b
#   return area

# length=int(input("Enter a length:"))
# breadth=int(input("enter a breadth of triangle"))
# a=rect(length,breadth)  
# print(a)

#approach 2:function with no return type and with no  parameter
#-----------------------------------------------

# def rect():
#   length=int(input("Enter a length:"))
#   breadth=int(input("enter a breadth of triangle"))
#   area=length*breadth
#   print(f"area of rectangle={area}")

# rect()

#approach 3:function with  no return type and with  parameter
#--------------------------------------------------
# def rect(l,b):
#   area=l*b
#   print(f"area of rectangle={area}")

# length=int(input("Enter a length:"))
# breadth=int(input("enter a breadth of triangle"))   
# rect(length,breadth)

#approach 4:function with  return type and with no  parameter
#--------------------------------------------
#area=l*b
# def rect():
#   length=int(input("Enter a length:"))
#   breadth=int(input("enter a breadth of triangle"))
#   area=length*breadth
#   return area

# a=rect()     
# print(f"area of triangle={a}")
#-----------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------
#sum and average list of numbers
# -----------------------------------------------------------------------------------------
#approach 1:function with return type and with parameter
#-----------------------------------
# def sumavg(lst):
#     s=0
#     for element in lst:
#         s=s+element
#         avg=s/len(lst)
#     else:
#         return s,avg   

# n=int(input("enter a range of for loop:"))
# l1 = []
# for i in range(n):
#     ele=int(input("enter a number in list: "))
#     l1.append(ele)
# a=sumavg(l1)

# print(f"sum of all element is {a[0]}")
# print(f"average of all element is {a[1]}")


#approach 2:function with no return type and with no  parameter
#-----------------------------------------------
# def getvalue():
#     n=int(input("enter how many  number we can take: "))
#     if (n<0):
#         print(f"it is invalid input {n}")
#     else:
#         lst=[]
#         for i in range(1,n+1,1):
#             number=int(input("enter a number:"))
#             lst.append(number)
#         else:
#             s=0
#             print("sum of all list element: ")
#             for element in lst:
#                 s=s+element   
#                 avg=s//len(lst)
#             else:
#                 print(lst)
#                 print(f"sum={s}")
#                 print(f"Average of all element:{avg}")
# getvalue()

#approach 3:function with  no return type and with  parameter
#--------------------------------------------------
# def sumavg(n,number,lst):
#     if n<0:
#         print(f"it is inavalid input{n}")
#     else:
#         s=0
#         for element in lst:
#             s=s+element
#             avg=s/len(lst)
#         else:
#             print(f"all elment in lst{lst}")
#             print(f"sum of all number={s}")
#             print(f"average of number is {avg}")

# r=int(input("enter a range of list: "))
# l=[]
# for i in range(r):
#     number=int(input("enter a number:"))
#     l.append(number)
# sumavg(r,number,l)

#approach 4:function with  return type and with no  parameter
#--------------------------------------------

# def sumavg():
#     n=int(input("Enter a range of element in list: "))
#     if n<0:
#         return "It is inavlid Input"
#     else:
#         lst=[]
#         for i in range(n):
#             number=int(input("enter a number: "))
#             lst.append(number)
#         else:
#             s=0
#             for element in lst:
#                 s=s+element
#                 avg=s+len(lst)
#             else:
#                 return lst,s,avg

# a=sumavg()
# print(f"all elemnt in list {a[0]}")    
# print(f"sum of all element is {a[1]}")
# print(f"average {a[2]}")

#which will accept a line of words and find length of each word and also find biggest word length
#----------------------------------------------------------------------------------------------------
#approach 1:function with return type and with parameter
#---------------------------------------------------------
# def getword(n,words):
#     if n<0:
#         print(f"it is invalid input{n}")
#     else:
#         return words

# def findlength(words):
#     dict1=dict()
#     for word in words:
#         dict1[word]=len(word)
#     return dict1

# def higgest(d1):
#     vals=d1.values()
#     mv=max(vals)
#     for key,values in d1.items():
#         if values==mv:
#             print(f"{key}{values}")
        


# r=int(input("enter a range of list: "))
# words=[]
# for i in range(r):
#     word=input(f"enter a word{i}")
#     words.append(word)
# res=getword(r,words)  
# print(f"all element in list: {words}")  

# r=findlength(res)
# print(r)

# higgest(r)

#approach 2:function with no return type and with no  parameter
#-----------------------------------------------
# def biggest():
#     n=int(input("enter a range of the word:"))
#     dict1=dict()
#     for i in range(1,n+1):
#         word=input(f"Enter a {i} word : ")
#         dict1[word]=len(word)
#     print(dict1)

#     val=dict1.values()
#     mv=max(val)
#     for key,values in dict1.items():
#         if values==mv:
#             print(f"{key }{values}")    
# biggest()


#approach 3:function with  no return type and with  parameter
# #--------------------------------------------------
# def getword(n,word):
#     if n<0:
#         print(f"It is invalid input{n}")
#     else:
#         return word   
    
# def biggest(d):
#     val=d.values()
#     mv=max(val)

#     for key,values in d.items():
#         if values==mv:
#             print(f"{key}  {values}")


# r=int(input("enter a range of list: "))
# dict1=dict()

# for i in range(r):
#     word=input(f"enter a word{i}")
#     dict1[word]=len(word)

# print(dict1)    

# res=getword(r,dict1)

# biggest(dict1)

#which will accept a line of words and find length of each word and also find biggest word length
#----------------------------------------------------------------------------------------------------
#approach 4:function with  return type and with no  parameter
#--------------------------------------------

# def getdata():
#     d1=dict()
#     n=int(input("Enter a Range of the String: "))
#     for i in range(1,n+1):
#         word=input("Enter a Number: ")
#         d1[word]=len(word)
    
#     val=d1.values()
#     mv=max(val)
#     for key ,value in d1.items():
#         if value == mv:
#             return d1,key,value

# res=getdata()
# print(f"Dict={res[0]}")
# print(f"{res[1]} {res[2]}")    
    


# which will accept a line of words and find length of each word and also find smallest word length
#-------------------------------------------------------------------------------------------------------------
#approach 1:function with return type and with parameter
#---------------------------------------------------------
#approach 2:function with no return type and with no  parameter
#-----------------------------------------------

# calculate roots of quandratic equation

# given input:     python is an oop lang
# expected output: nohtyp si na poo gnal
#approach 1:function with return type and with parameter
#---------------------------------------------------------
# def reverse_str(s):
#     a=s.split()
#     reverse_string=[]

#     for i in a:
#         rs=i[::-1]
#         reverse_string.append(rs)
#     return reverse_string    

# s1=input("enter a string:")
# res=reverse_str(s1)
# print(res)    

#approach 2:function with no return type and with no  parameter
#-----------------------------------------------
# def reverse_str():
#     s=input("Enter a string : ")
#     a=s.split()
#     reversed_list=[]

#     for i in a:
#         b=i[::-1]
#         reversed_list.append(b)
#     print(reversed_list)   

# reverse_str()    


#decide magic number or not

# a=int(input("Enter a number: "))
# sqr=a*a
# s=str(a)
# ends=s.endswith("{a}")
# if ends==True:
#     print("it is magic number:")
# else:
#     print("it is not magic number;")
# 5=25
# 6=36
# 15=225


# squares = [i for i in range(1,31,1)]
# print(squares)



def dispvalues(**kvr): # Here **kvr is called Var-Length Keyword arg and whose type <class,dict>
	print(kvr,type(kvr))



#Main Program
dispvalues(sno=100,sname="RS",marks=45.67) # Function Call-1 with 3 Key Word Arguments
dispvalues(eno=200,ename="TR",job="SE",sal=8.0) # Function Call-2 with 4 Key Word Arguments
dispvalues(tno=300,tname="JH",sub1="Python",sub2="Java",sub3="DSA") # Function Call-3 with 5 Key Word Arguments
dispvalues(cid=400,cname="DR")# Function Call-4 with 2 Key Word Arguments
dispvalues(stno=1000,sname="SS",hb1="Eating",hb2="Sleeping",hb3="Chatting",hb4="Roaming") # # Function Call-5 with 6 Key Word Arguments