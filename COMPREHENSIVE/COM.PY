#KVR SIR EXAMPLE
# #Program Obtaining List of +Ve Values from List of Numerical Values
# #GeneratorComprehensionEx.py

# lst=[10,-20,30,-40,67,-12,-45,0,56,-45,2,-5,-5]
# ps=(val  for val in lst   if val>0 ) # here ps is an object of <class,'generator'>
# #Convert generator object into tuple
# pse=tuple(ps)
# print(pse,type(pse))
# #---------------------------------------------------------------------------------

# #Program for Reading the Values from KBD by using Comprehension Tech
# #ListComprehenReadValuesEx.py
# lst=[int(val)  for val in input("Enter List of Values Separated by space:").split()]
# print(lst,type(lst))


# lst1=[vals for vals in input("Enter list of values:").split() if int(vals)%2==0]
# print(lst1)
# #--------------------------------------------------------------------------------------

# #Program Obtaining List of +Ve Values from List of Numerical Values
# #ListComprehensionEx1.py
# lst=[10,-20,30,-40,67,-12,-45,0,56,-45,2,-5,-5]

# pslist=[ val  for val in lst   if val>0 ]

# nglist=[val for val in lst if val<0]
# print("List of +Ve Vals=",pslist,type(pslist))
# print("List of -Ve Vals=",nglist,type(nglist))
# #-------------------------------------------------------------------------------------------

# #Program for Obtaining List of -Ve Values from List of Combination +ve and -ve vals
# #ListComprehensionEx2.py
# neglst=[ float(val)   for val in input("Enter list of Vals separated by space:").split() if float(val)<0 ]
# print("List of -Ve Values")
# print(neglst)
# #----------------------------------------------------------------------------------------------

# #program for Finding Square Root for +Ve Numbers from List of Numerical Values
# #DictComprehensionEx2.py
# print("Enter List of Values separated by Space:")
# ovals=[float(val) for val in input().split() if float(val)>0]
# sqrtvals=[float(val)**0.5 for val in ovals]

# print("="*50)
# print("Given Value\t\tSquareRoot Value")
# print("="*50)

# for val1,val2 in zip(ovals,sqrtvals):
#     print("\t{}\t\t{}".format(val1,round(val2,2)))
# print("="*50)
# #------------------------------------------------------------------------------------------

# #Program for Deciding whether the given number is Prime or Nor from List of Numbers
# #ListComprehensionEx4.py
# def decideprime(val):
#     res=1
#     for i in range(2,val):
#         if(val%i==0):
#             res=0
#             break
#     return res

# #Main Program
# print("Enter List of Values Seeperated by space:")
# vals=[int(val) for val in input().split() if int(val)>1]

# primes=[ val   for val in vals  if decideprime(val) ]

# print("List of Given Values:{}".format(vals))
# print("List of Primes:{}".format(primes))
# #-------------------------------------------------------------------

# #Program Obtaining List of +Ve Values from List of Numerical Values
# #SetComprehensionEx1.py
# lst=[10,-20,30,-40,67,-12,-45,0,56,-45,2,-5,-5]

# pslist= { val  for val in lst   if val>0 }

# nglist= {val for val in lst if val<0}
# print("List of +Ve Vals=",pslist,type(pslist))
# print("List of -Ve Vals=",nglist,type(nglist))
# #------------------------------------------------------------------

# #Program for Finding Square for Every Value of list of values
# #DictComprehensionEx1.py
# lst=[3,13,12,9,17,4,3]
# d={val:val**2 for val in lst }
# print(d,type(d))
# #------------------------------------------------------------------------

# #program for Finding Square Root for +Ve Numbers from List of Numerical Values
# #DictComprehensionEx2.py
# print("Enter List of Values separated by comma:")
# sqrtvals={float(val):round(float(val)**0.5,2)  for val in input().split(",")  if float(val)>0 }
# print("="*50)
# print("Given Value\t\tSquareRoot Value")
# print("="*50)
# for val1,val2 in sqrtvals.items():
#     print("\t{}\t\t{}".format(val1,val2))
# print("="*50)
# #----------------------------------------------------------------------------------------------


# PRACTICE EXAMPLE
#-------------------------------------------------------------------------


#listcomprehension

# lst=[ int(i)*int(i) for i in input("Enter a list values:  ").split()]
# print(lst)

# set1={ int(val)**2  for val in input("Enter a values:  ").split()}
# print(set1)

# dict1={int(val):int(val)*int(val) for val in input("Enter A number: ").split()}
# print(dict1)

# tpl=(int(val) for val in input("Enter A number: ").split())
# print(tpl)
# t1=tuple(tpl)
# print(t1)
#------------------------------------------------------------------------------

def decideprime(val):
    res="it is prime"
    for i in range(2,val):
        if(val%i==0):
            res="Not"
            break
    return res

#Main Program
print("Enter List of Values Seeperated by space:")
vals=[int(val) for val in input().split() if int(val)>1]

primes=[ val   for val in vals  if decideprime(val) ]

print("List of Given Values:{}".format(vals))
print("List of Primes:{}".format(primes))

# #----------------------------------------------------------------
# def decideprime(val):
#     res=1
#     for i in range (2,val):
#         if (val%i==0):
#             res=0
#             break
#     return res 

# vals=[int(val) for val in input().split() if int(val)>1]

# primes=[val for val in vals if decideprime(val)]

# print("List of Given Values:{}".format(vals))
# print("List of Primes:{}".format(primes))
# #--------------------------------------------------------