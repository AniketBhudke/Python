# #relational operator(>,<,==,!=,>=,<=)

# #int
a = 5
b = 10

# Relational operations
print(a > b)   # False
print(a < b)   # True
print(a == b)  # False
print(a != b)  # True

# #float
# x = 3.14
# y = 2.71

# # Relational operations
# print(x >= y)  # True
# print(x <= y)  # False
# print(x == y)  # False
# print(x != y)  # True

# #complex
# complex1 = 2 + 3j
# complex2 = 1 + 4j

# # Relational operations will raise an error
# # print(complex1 > complex2)  # TypeError

# # You can only check equality or inequality
# print(complex1 == complex2)  # False
# print(complex1 != complex2)  # True

# #str
# str1 = "apple"
# str2 = "banana"

# # Relational operations (lexicographical comparison)
# print(str1 > str2)   # False ('apple' comes before 'banana')
# print(str1 < str2)   # True
# print(str1 == str2)  # False
# print(str1 != str2)  # True

#chr return alphabhet of perticular value
print(chr(78))
print(ord("S"))

# #boolean
# bool1 = True
# bool2 = False

# # Relational operations
# print(bool1 > bool2)   # True (True is considered 1, False is 0)
# print(bool1 == bool2)  # False
# print(bool1 != bool2)  # True

# #list
# list1 = [1, 2, 3]
# list2 = [1, 2, 4]

# # Relational operations
# print(list1 > list2)   # False (compares element by element)
# print(list1 < list2)   # True
# print(list1 == list2)  # False
# print(list1 != list2)  # True

# #tuple
# tuple1 = (5, 10)
# tuple2 = (5, 8)

# # Relational operations
# print(tuple1 > tuple2)   # True (compares element by element)
# print(tuple1 == tuple2)  # False
# print(tuple1 != tuple2)  # True

# #dict
# dict1 = {"a": 1, "b": 2}
# dict2 = {"a": 1, "b": 3}

# # Trying relational operations directly would result in a TypeError
# # print(dict1 > dict2)  # TypeError: '>' not supported between instances of 'dict'

# # You can compare individual values within the dictionaries
# print(dict1["b"] > dict2["b"])  # False

# #set
# set1 = {1, 2, 3}
# set2 = {2, 3, 4}

# # Set comparisons using relational operators will raise an error
# # print(set1 > set2)  # TypeError

# # Set operations for comparison
# print(set1 == set2)         # False (they have different elements)
# print(set1 != set2)         # True
# print(set1.issubset(set2))  # False
# print(set1.issuperset(set2))  # False

# #bytes
# byte1 = b'abc'
# byte2 = b'xyz'

# # Relational operations
# print(byte1 < byte2)  # True (because 'a' < 'x' lexicographically)
# print(byte1 > byte2)  # False
# print(byte1 == byte2)  # False

# #bytearray
# bytearray1 = bytearray(b'abc')
# bytearray2 = bytearray(b'xyz') #ascii value

# # Relational operations
# print(bytearray1 < bytearray2)  # True (same as with bytes)
# print(bytearray1 == bytearray2)  # False
# print(bytearray1 != bytearray2)  # True

# #range
# range1 = range(1, 5)
# range2 = range(1, 10)

# # Range objects cannot be compared directly using relational operators
# # print(range1 < range2)  # TypeError

# # You can convert ranges to lists or tuples for comparison
# print(list(range1) < list(range2))  # True, because the elements in range1 are fewer

# #frozenset
# frozenset1 = frozenset({1, 2, 3})
# frozenset2 = frozenset({2, 3, 4})

# # Frozenset comparisons
# print(frozenset1 == frozenset2)  # False
# print(frozenset1 != frozenset2)  # True
# print(frozenset1.issubset(frozenset2))  # False
# print(frozenset1.issuperset(frozenset2))  # False
