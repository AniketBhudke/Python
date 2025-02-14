# sum=n*(n+1)//2#n is any number




# ------------------------------------------------------------------------------
#                           Data type in python
# ------------------------------------------------------------------------------

# 1.Fundamental data type
# ------------------------------------------------------------------------------
# a.int 
# b.float
# c.complex
# d.bool

# ------------------------------------------------------------------------------
#2.sequntial data type 
# ------------------------------------------------------------------------------
# a.str
# b.range
# c.bytes
# d.bytesarray

# ------------------------------------------------------------------------------
#3.set category data type
# ------------------------------------------------------------------------------
# a.set -------------16
# b.frozenset -------8

# ------------------------------------------------------------------------------
# 4.list category data type
# ------------------------------------------------------------------------------
# a.tuple ----2
# b.list -----13

# ------------------------------------------------------------------------------
# 5.Dict category data type
# ------------------------------------------------------------------------------
# a.dict ------8

# ------------------------------------------------------------------------------
# 6.nontype category data type
# ------------------------------------------------------------------------------
# a.NoneType

#-------------------------------------------------------------------------------
#STRING
#-------------------------------------------------------------------------------
# 1) capitalize()
# 2) title()
# 3) swapcase()
# 4) lower()
# 5) upper()
# 6) count()
# 7) islower()
# 8) isupper()
# 9) isdigit()
# 10) isalpha()
# 11) isalnum()
# 12) split()   OR  split("delimeter")
# 13) join(Iterable Object)
# 14) index()
# 15) lstrip()
# 16) rstrip()
# 17) strip()
# 18) startswith()
# 19) endswith()

# ------------------------------------------------------------------------------
# LIST
# ------------------------------------------------------------------------------
# 1.append()
# 2.insert()
# 3.clear()
# 4.remove()
# 5.pop(index)
# 6.pop()
# 7.del opearator
# 8.index()
# 9.copy()
# 10.count()
# 11.reverse()
# 12.sort()
# 13.extend()

# ------------------------------------------------------------------------------
# Tuple
# ------------------------------------------------------------------------------
# 1.index()
# 2.count()

# ------------------------------------------------------------------------------
# set
# ------------------------------------------------------------------------------
# 1.add()
# 2.remove()
# 3.discard()
# 4.pop()
# 5.clear()
# 6.copy()
# 7.isdisjoint()
# 8.issuperset()
# 9.issubset()
# 10.union()
# 11.intersection()
# 12.difference()-------------------s3=s1.difference(s2)---pahile ya set.i.e s1, madale unique element dete
# 13.symmentric_difference()-------------------------------doni ya madle unique element return krte 3rd set mde
# 14.symmentric_difference_update()------------------------doni ya madle unique element return krte ,1st set mde
# 15.symmentric update()----------------------------------s3 gya ch .kam nhi je pn ahe tya cha answer s1 mde ch return krte
# 16.update--------------------update krte . chya aadhi chya set le

# ------------------------------------------------------------------------------
#frozenset
# ------------------------------------------------------------------------------
# 1.copy()
# 2.isdisjoint()
# 3.issuperset()
# 4.issubset()
# 5.union()
# 6.intersection()
# 7.difference()
# 8.symmentric_difference()

# ------------------------------------------------------------------------------
#Dict
# ------------------------------------------------------------------------------
# 1.clear()
# 2.pop()
# 3.popitem()
# 4.copy()
# 5.get()
# 6.keys()
# 7.values()
# 8.items()

#----------------------------------------------------------------------------------
#                           combination of datatype
#----------------------------------------------------------------------------------
# #dict
# ------------
# dict in dict---Possible
# list in dict---Possible
# tuple in dict--Possible
# set in dict---possible

# ---------------------
# List
# ---------------------
# list in list---Possible
# tuple in list---Possible
# set in list-----Possible
# dict in list-----Possible

# --------------------------------------
# tuple
# --------------------------------------
# tuple in tuple---Possible
# list in tuple---Possible
# set in tuple--Possible
# dict in tuple---Possible

# -------------------------------------------
# Set
# ------------------------------------------
# set in set----Not Possible---TypeError--Unhashable Type
# list in set----Not Possible---TypeError--Unhashable Type
# tuple in set----Possible
# dict in set-----Not Possible---TypeError--Unhashable Type
   
#------------------------------------------------------------------------
#                       Mutable and immutable
#-----------------------------------------------------------------------
#1.Mutable
#------------
# =>A Mutable Object is one, whose content can be changed / Updated / Modified at SAME Address.

# Examples: list,bytearray,set,dict.     -----LBSD----

# ---------------------
# 2.Immutable Object
# ----------------------
# =>An Immutable Object is one, which Satisfies the following Properties
		
# 		1. Immutable Object Value Can't be chaged At Same Address 
# 			(Value can be changed and changed Value placed in New Address)
# 		2. Immutable Object does not allows us to perfrom Item Assigment.
# Examples:  int, float, bool,complex,str,bytes,range,tuple,set,frozenset,NoneType.

# ------------------------------------------------------------------------------
#                            print have 6 syntax 
# ------------------------------------------------------------------------------

# ------------------------------------------------------------------------------
#  1.display one value or multiple value on console
# ------------------------------------------------------------------------------
# a=10
# b=20
# print(a,b)

# ------------------------------------------------------------------------------
# 2.string as user-prompting msg
# ------------------------------------------------------------------------------
# s="python"
# a=3.12
# print("hello")
# print(a+str(a))

# ------------------------------------------------------------------------------
# 3.display message cum values 
# ------------------------------------------------------------------------------
# a=10
# print("val of a:",a)

# ------------------------------------------------------------------------------
# # 4.display msg using format() function
# ------------------------------------------------------------------------------
# a=10
# print("val of a={}",format(a))

# ------------------------------------------------------------------------------
# 5.by using letter f
# ------------------------------------------------------------------------------
# a=10
# b=20
# c=a+b
# print(f"sum of {a} and {b}= {c}")

# ------------------------------------------------------------------------------
# 6.format specifier
# ------------------------------------------------------------------------------
# a=10
# b=20
# c=a+b
# print("sum of %d and %d = %d" &(a,b,c))

# ------------------------------------------------------------------------------
# 7.iterable object in the same line(Horizontal line)
# ------------------------------------------------------------------------------
# for val in range(10,21,2):
#     print(val,end="  ")

# ------------------------------------------------------------------------------------------------------------
#                       Seven type of operator
# --------------------------------------------------------------------------------------------------------------

#                                  1.Arithmatic operator
# ---------------------------------------------------------------------------------------------------------
# 	SLNO		SYMBOL			MEANING			EXAMPLES  a=10  b=3
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# 	1.				+			Addition				print(a+b)-------- 13
	
# 	2.				-			Substraction			print(a-b)----------7
	
# 	3.				*			Multiplication			print(a*b)----------30

# 	4.				/			Division				print(a/b)----------3.3333333333333335
# 							   (Float Quotient)

# 	5.				//			Floor Division		print(a//b)---------3   6 2
# 							   (Integer Quotient)

# 	6.				%			Modulo Division		print(a%b)---------1
# 								(Remainder)
								
# 	7.				**			Exponentiation		print(a**b)---------1000
# 								(power )

#-----------------------------------------------------------------------------------------------------------
#                            2.Assignment operator
# ------------------------------------ ----------------------------------------------------------------------
#1. Single Line Assigment   2. Multi Line Assigment


#-----------------------------------------------------------------------------------------------------
#               3.Relational opeartor(comparison operator)(Test cond) ord("a") chr(97)
#-----------------------------------------------------------------------------------------------------
# SLNO		SYMBOL			MEANING			EXAMPLES  
# ------------------------------------------------------------------------------------------------------------------------------------------------------------
# 1.			>			greater than		print(10>2)--------------True
# 												print(10>20)------------False

# 2.			<			less than			print(10<20)------------True
# 												print(10<5)--------------False

# 3.			==			comparision			print(10==10)----------True
# 						    (double equal to)	print(10==20)----------False

# 4.			!=			not equal to		print(10!=10)-----------False
# 												print(10!=20)-----------True

# 5.			>=			greater than		print(10>=20)-----------False
# 							or equal to			print(10>=5)-----------True

# 6.			<=			less than			print(10<=5)-----------False
# 							or equal to			print(10<=20)---------True


#----------------------------------------------------------------------------------------------------
#                       4.Logical Operator(comparison opearotor)
#--------------------------------------------------------------------------------------------------------
# SLNO		SYMBOL			MEANING
# -----------------------------------------------------------------------------------------------------------------------------------------------------------
# 	1.			and				Physical ANDing
# 	2.			or				Physical ORing
# 	3.			not				------------------------

#------------------------------------------------------------------------------------------------------------
#                            5.Bitwise operator
#-----------------------------------------------------------------------------------------------------------
#      SLNO			   SYMBOL			MEANING
# -------------------------------------------------------------------------------------------------------------------------------------------------------------------
# 		1				<<				Bitwise Left Shift Operator    a=10 b=2   10*2 power 2 =40
# 		2				>>				Bitwise Right Shift Operator    10/2 power 2  10/4  =2
# 		3.				|				Bitwise OR Operator            addition    union
# 		4.				&				Bitwise AND Operator            multiplication    interection
# 		5.				~				Bitwise Complement Operator
# 		6.				^				Bitwise XOR Operator            same same 0 ,different 1
# #------------------------------------------------------------------------------------------------------------
# Even: A number n is even if n & 1 == 0.
# Odd: A number n is odd if n & 1 == 1
print(99&1==0)
# 6.Membership Opeartor
    #   a. in operator
    #   b. not operator
# 7.identity operator
    #   a. is operator ------------doni obj jr same=true,different=false,immutable-same address--,mutable--different address
        # dict --------->Not Possible
        # list --------->Not Possible
        # set ---------->Not Possible
        # Dict --------->Not Possible      --------------------
        # Tuple -------->Not Possible                          |
        # Str ---------->Possible                              |
        # NoneType ----->Possible                              |
        # Int ---------->Possible                              |------------Str,NoneType,Int,Boolean
        # Float -------->Not Possible                          |
        # Complex ------>Not Possible                          |
        # Boolean ------>Possible                              |
        # Bytes -------->Not Possible     ---------------------
        # Bytearray ---->Not Possible

 
    #   b. is not operator --------doni object jr same=false,different=true

# ------------------------------------------------------------------------------ 
# 
# comprehension
#list comprehension
# lst=[22,3,4,5,6,7,8]
# lst1=[val for val in lst if val%2==0 ]
# print(lst1)

# lst=[[1,2,3],[4,5,6],[7,8,9]]
# l1=[value for lists in lst for value in lists]
# print(l1)

# lst=[[1,2,3],[4,-5,6],[7,-8,9]]
# l1=[value for lists in lst for value in lists if value>0]
# print(l1)

# lst=[1,2,3,4,5,6]
# l1=[value**2 if value%2==0  else value**3 for value in lst]
# print(l1)

# lst=[11,-2,4,6,0,-5,66,-8]
# l2=["positive" if value>2==0 else "negative" for value in lst]
# print(l2)


#AttributeError
# x = 5
# x.append(10)
# AttributeError: 'int' object has no attribute 'append'
