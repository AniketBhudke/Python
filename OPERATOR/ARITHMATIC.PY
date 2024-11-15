# operator (+,-,*,/,//,%,**,)
#/---- float mde output division ch 
#//----integer mde output division ch
#%-----Remainder
#**----Exponentiation

#int data
# print(10 + 12)
# a=5
# b=45
# print(a+b)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a//b)
# print(a%b)
# print(a**b)

#float
# a= 1.2 
# b= 3.6
# # print(1.2 + 1.2)
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)
# print(a ** b)

#complex
# a=2+3j
# b=4+5j
# print(2+4j + 3+ 5j)
# print(a-b)
# print(a * b)
# print(a / b)
# print(a // b) #--------------------TypeError: unsupported operand type(s) for //: 'complex' and 'complex'
# print(a % b)#-----------------------TypeError: unsupported operand type(s) for //: 'complex' and 'complex'
# print(a ** b)#----------------------TypeError: unsupported operand type(s) for //: 'complex' and 'complex'

# #boolean
# a=True
# b=True
# print(True + True) #---2
# print(True + False) #---1
# print(False + False)#---0
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)
# print(a ** b)

#str
# a='kunal'
# b='sagar'
# print("kunal" + "sagar")
# print(a - b)
# print(a * b)
# print(a / b)
# print(a // b)
# print(a % b)
# print(a ** b)

#list
# list1=[12,13,14,23]
# list2=[12,13,14,23]
# # print(list1 + list2)
# print(list1 - list2) #-------------TypeError: unsupported operand type(s) for -: 'list' and 'list'

#set--------------------unsupported operand type(s) for +: 'set' and 'set'
# set1={1,2,3,4,5}
# set2={12,13,55,667,88}
# s=set1 + set2 
# print(s)

#FROZENSET-------------TypeError: unsupported operand type(s) for +: 'frozenset' and 'frozenset'
# set1={1,2,3,4,5}
# set2={12,13,55,667,88}
# fs1=frozenset(set1)
# fs2=frozenset(set2)
# print(fs1 + fs2)

#TUPLE
# t1=(1,2,3,4,5)
# t2=(11,12,13,14,15)
# print(t1 + t2)

#BYTES
# A={1,2,3,4,5,55}
# B={11,12,13,14,15,155}
# byt1=bytes(A)
# byt2=bytes(B)
# print(byt1)
# print(byt2)
# print(byt1 + byt2)

#BYTEARRAY
# byta1=bytearray(A)
# byta2=bytearray(B)
# print(byta1 + byta2)

#RANGE---------------------TypeError: unsupported operand type(s) for +: 'range' and 'range'
# a=range(1,10,1)
# b=range(2,33,2)
# print(a + b)

#dict--------------------unsupported operand type(s) for +: 'dict' and 'dict'
# d1={1:"one",2:"two",3:"three",4:"four"}
# d2={11:"one",12:"two",13:"three",14:"four"}
# print(d1 + d2)