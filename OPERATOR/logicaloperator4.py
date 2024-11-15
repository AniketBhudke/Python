#logical operator(and ,or,not)

#int
# a = 0
# b = 5

# # Logical operations
# print(a and b)  # 0 (because `a` is falsy, and with `and`, it returns the first falsy value)
# print(a or b)   # 5 (because `a` is falsy, so it returns `b` as the truthy value)
# print(not a)    # True # a is zero so it is false ,not convert into true
# print(not b)    # False # b is non zero value so it is true so not convert into false 
#----------------------------------------------------------------------------------------------------------------------

#float
x = 0.0
y = 3.14

# Logical operations
print(x and y)  # 0.0 (because `x` is falsy)
print(x or y)   # 3.14 (because `x` is falsy, so it returns the truthy `y`)
print(not y)    # False (`y` is truthy, so `not` returns False)
#-----------------------------------------------------------------------------------------------------------------------------

#str
str1 = ""
str2 = "Hello"

# Logical operations
print(str1 and str2)  # "" (because `str1` is falsy)
print(str1 or str2)   # "Hello" (because `str1` is falsy, so it returns `str2`)
print(not str1)       # True (`str1` is falsy, so `not` returns True)
print(not str2)       # False (`str2` is truthy)
#--------------------------------------------------------------------------------------------------------------------------

#boolean
bool1 = True
bool2 = False

# Logical operations
print(bool1 and bool2)  # False (since `bool2` is False)
print(bool1 or bool2)   # True (since `bool1` is True)
print(not bool1)        # False (`not` flips the True value)
#--------------------------------------------------------------------------------------------------------------

#list
list1 = []
list2 = [1, 2, 3]

# Logical operations
print(list1 and list2)  # [] (because `list1` is falsy)
print(list1 or list2)   # [1, 2, 3] (because `list1` is falsy, so it returns `list2`)
print(not list1)        # True (because `list1` is falsy)
print(not list2)        # False (because `list2` is truthy)
#---------------------------------------------------------------------------------------

#tuple
tuple1 = ()
tuple2 = (4, 5, 6)

# Logical operations
print(tuple1 and tuple2)  # () (because `tuple1` is falsy)
print(tuple1 or tuple2)   # (4, 5, 6) (because `tuple1` is falsy, so it returns `tuple2`)
print(not tuple1)         # True (because `tuple1` is falsy)
print(not tuple2)         # False (because `tuple2` is truthy)
#------------------------------------------------------------------------------------------------

#dict
dict1 = {}
dict2 = {"a": 1, "b": 2}

# Logical operations
print(dict1 and dict2)  # {} (because `dict1` is falsy)
print(dict1 or dict2)   # {"a": 1, "b": 2} (because `dict1` is falsy, so it returns `dict2`)
print(not dict1)        # True (because `dict1` is falsy)
print(not dict2)        # False (because `dict2` is truthy)
#--------------------------------------

#sets
set1 = set()
set2 = {1, 2, 3}

# Logical operations
print(set1 and set2)  # set() (because `set1` is falsy)
print(set1 or set2)   # {1, 2, 3} (because `set1` is falsy, so it returns `set2`)
print(not set1)       # True (because `set1` is falsy)
print(not set2)       # False (because `set2` is truthy)
#-------------------------------------------------------------------

#byte and bytearray
byte1 = bytearray(b'')
byte2 = bytearray(b'abc')

# Logical operations
print(byte1 and byte2)  # bytearray(b'') (because `byte1` is falsy)
print(byte1 or byte2)   # bytearray(b'abc') (because `byte1` is falsy)
print(not byte1)        # True (because `byte1` is falsy)
print(not byte2)        # False (because `byte2` is truthy)
#----------------------------------------------------------------------------

#range
range1 = range(0)
range2 = range(1, 10)

# Logical operations
print(range1 and range2)  # range(1, 10) (because `range1` is truthy)
print(range1 or range2)   # range(0, 0) (returns `range1` because ranges are truthy)
print(not range1)         # False (range objects are always truthy)
#-----------------------------------------------------------

#complex
complex1 = 0 + 0j
complex2 = 1 + 2j

# Logical operations
print(complex1 and complex2)  # 0j (because `complex1` is falsy)
print(complex1 or complex2)   # (1+2j) (because `complex1` is falsy, so it returns `complex2`)
print(not complex1)           # True (because `complex1` is falsy)
print(not complex2)           # False (because `complex2` is truthy)
#-------------------------------------------------------------------------