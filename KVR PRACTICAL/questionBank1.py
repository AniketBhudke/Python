# All students are requested to slove the following Questions
# 	================================================================
# 1. Write a Python program to sum all the items in a list. 
# lst=[11,12,13,14,15,16,17]
# s=0
# for number in lst:
#     s=s+number
# print(s)    

# 2. Write a Python program to multiply all the items in a list. 
# lst=[11,12,13,14,15,16,17]
# for number in lst:
#     print(f"{number}*{number}={number*number}")

# 3. Write a Python program to get the largest number from a list. 
# lst=[11,12,13,14,15,16,17]
# lar=4
# for number in lst:
#     if lar < number:
#         lar=number
# print(lar)    

# 4. Write a Python program to get the smallest number from a list.
# lst=[11,12,13,14,15,16,17]
# small=12
# for number in lst:
#     if small > number:
#         small=number
# print(small)        

# 5. Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings. 
# 		Sample List : ['abc', 'xyz', 'aba', '1221']
# 		Expected Result : 2
# S=['abc', 'xyz', 'aba', '1221']
# count=0
# for string in S:
#     if len(string)>=2 and string[0] == string[-1]:
#         count=count+1
# print(count)        

# 6. Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples. 
# 	Sample List : [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# 	Expected Result : [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

# Lst1=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
# for i in range(len(Lst1)):
#     for j in range(i+1,len(Lst1)):
#         if Lst1[i][-1]>Lst1[j][-1]:
#             Lst1[i],Lst1[j]=Lst1[j],Lst1[i]
# print(Lst1)

# a=10
# b=5
# x=a
# a=b
# b=x

# print(a,b)
# l1 = [1,24,3,44,5,64,7,8,9]
# for i in range(len(l1)):
#     for j in range(len(l1)):
#         if l1[i]>l1[j]:
#             l1[i],l1[j]=l1[j],l1[i]
# print(l1)

# 7. Write a Python program to remove duplicates from a list. #s+rs
# lst=[1,1,21,2,2,13,1,3,2,13,33]
# lst1=[]
# for element in lst:
#     if  element  not in lst1 :
#         lst1.append(element)
# print(lst1)

# print(list(set(lst)))


# 8. Write a Python program to check a list is empty or not. #s
# lst=[]
# if len(lst)>0:
#     print("List is not Empty")
# else:
#     print("list is Empty")    

# 9. Write a Python program to clone or copy a list.#s
# list1=[1,2,3,4,6,0,66,9]
# lst=list1
# print(lst)

# 10. Write a Python program to find the list of words that are longer than n from a given list of words. 


# 11. Write a Python function that takes two lists and returns True if they have at least one common member.#s

# def common_number(lst1,lst2):
#     for i in range(len(lst1)-1):
#         for j in range (len(lst2)-1):
#             if l1[i]==l2[j]:
#                 return "True"
#             else:
#                 return "False"    

# l1=[12,13,14,15]
# l2=[12,2,3,4,5]
# res=common_number(l1,l2)
# print(res)

# 12. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements. #s+c
# 		Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# 		Expected Output : ['Green', 'White', 'Black']
# sample=['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
# rmv=[sample[0],sample[4],sample[5]]
# # print(len(sample))
# # print(sample[4])
# print(sample[5])
# for i in range(len(sample)-1,-1,-1):
#     if sample[i] in rmv:
#         sample.remove(sample[i])``
#         print(sample)       

# sample.remove(sample[5])
# sample.remove(sample[4])
# sample.remove(sample[0])
# print(sample)

# 13. Write a Python program to generate a 3*4*6 3D array whose each element is *.
 

# 14. Write a Python program to print the numbers of a specified list after removing even numbers from it. #s
# list1=[12,13,14,15,2,4,6,8,10]
# even=[]
# for number in list1:
#     if number%2==0:
#         even.append(number)
# print(even)        


# 15. Write a Python program to shuffle and print a specified list.

# 16. Write a Python program to generate and print a list of first and last 5 elements where the values are square of numbers between 1 and 30 (both included).
# sqrt_lst=[] 
# for i in range(1,31,1):
#     if 0<i<=5 or 25<=i<=30:
#         sqrt=i*i
#         sqrt_lst.append(sqrt)
# print(sqrt_lst)    

# 17. Write a Python program to generate and print a list except for the first 5 elements, where the values are square of numbers between 1 and 30 (both included).
# sqrt_lst=[] 
# for i in range(1,31,1):
#     if i>5:
#         sqrt=i*i
#         sqrt_lst.append(sqrt)
# print(sqrt_lst)    


# 18. Write a Python program to generate all permutations of a list in Python.

# 19. Write a Python program to get the difference between the two lists. 
# l1=[1,2,3,4,5,6]
# l2=[1,2,11,12,13,14,15,16]
# l3=[]

# for i in range(len(l1)):
#     for j in range(len(l2)):
#         if l1[i]==l2[j] :                             #1!=1  1!=2   1!=11      1!=12   1!=13   1!=14   1!=15   1!=16
#             l3.append(l2[i])                          #2!=1  2!=2   2!=11      2!=12   2!=13   2!=14   2!=15   2!=16              
# print(l3)            

# Input : test_list = [(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]
# Output : [(5, 6, 7, 8), (6, 10), (7, 13)]

# lst=[(5, 6), (5, 7), (5, 8), (6, 10), (7, 13)]
# l=[]
# for element in lst:
#     l.append(list(element))
# print(l)
# # l=[[5, 6], [5, 7], [5, 8], [6, 10], [7, 13]]
# for i in range(len(l)):    
#     for j in range(i+1,len(l)):
#         if l[i][0]==l[j][0]:
#             l[i]=l[i]+[l[j][1]]
# print(l)                    
            

# 20. Write a Python program access the index of a list. 

# 21. Write a Python program to convert a list of characters into a string.
# lst=[['p','y','t','h','o','n'],['a','b','c']]
# a=str(lst[0])
# print(a)
# 22. Write a Python program to find the index of an item in a specified list. 
# lst=[11,12,13,14,15,16,17]
# l=lst.index(12)
# print(l)
# s=16
# for i in range(len(lst)):
#     if lst[i]==s:
#         print(i)

# 23. Write a Python program to flatten a shallow list. 
# lst=[[11,12,13],[14,15,16],[17,18,19]]
# l=[]
# for subobj in lst:
#     for element in subobj:
#         l.append(element)
# print(l)             

# 24. Write a Python program to append a list to the second list. 
# lst=[11,12,13,14,15,16,17,18]
# l=[]
# for element in lst:
#     l.append(element)
# print(l)    

# 25. Write a Python program to select an item randomly from a list. 
# import random

# # List of items
# items = ['apple', 'banana', 'cherry', 'date', 'elderberry']

# # Select a random item from the list
# random_item = random.choice(items)

# # Print the randomly selected item
# print("Randomly selected item:", random_item)

# 26. Write a python program to check whether two lists are circularly identical.
# lst1=[11,12,13,14,15,15,16,17,18]
# lst2=[11,12,13,14,15,15,16,17,18]
# if lst1==lst2:
#     print("it is identical element")
# else:
#     print("it is not identical")    

# 27. Write a Python program to find the second smallest number in a list. 
# lst=[11,12,13,14,15,16,17,18]
# small=14
# second=1
# for element in lst:
#     if element<small:
#         small=element
# print(small)  

# for element in lst:        
#     if small>element>second:#max1>num>second_large:  
#         second=element
#     print(second)        


# 28. Write a Python program to find the second largest number in a list. 

# 29. Write a Python program to get unique values from a list. 
# lst=[1,2,3,4,5,6,7,8,1,2,4]
# new_lst=[]
# for value in lst:
#     if value not in new_lst:
#         new_lst.append(value)
# print(new_lst)

# 30. Write a Python program to get the frequency of the elements in a list. 
# lst=[1,2,3,4,5,2,2,3,4,5]
# dict1={}
# for value in lst:
#     dict1[value]=lst.count(value)
# print(dict1)    
# for key,value in dict1.items():
#     print( f"{key} \t\t {value}")

# 31. Write a Python program to count the number of elements in a list within a specified range.
# lst=[1,2,3,4,5,2,2,3,4,5]
# dict1={}
# for value in lst:
#     if value<5:
#         dict1[value]=lst.count(value)
# print(dict1)    
# for key,value in dict1.items():
#     print( f"{key} \t\t {value}")


# 32. Write a Python program to check whether a list contains a sublist.
# lst=[1,2,[1,2,3,4],[11,12,13,14],[21,22,23,24,25]]
# for value in lst:
#     if type(value)!=int:
#         print(value)

# 33. Write a Python program to generate all sublists of a list. 


# 35. Write a Python program to create a list by concatenating a given list which range goes from 1 to n. 
# 	Sample list : ['p', 'q']
# 	n =5
# 	Sample Output : ['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4', 'p5', 'q5']

# sample=['p', 'q']
# expected=[]
# n=int(input("Enter a range:"))
# for char in sample:
#     for i in range (1,n):
#         expected.append(char+str(i))
# print(expected)        

# 36. Write a Python program to get variable unique identification number or string. 

# 37. Write a Python program to find common items from two lists.
lst1=[1,12,3,4,55,66,78]
lst2=[12,23,434,56,78,90]
#logic1
# for val1 in lst1:
#     for val2 in lst2:
#         if val1==val2:
#             print(val1)
#logic2
# lst3=set(lst1).intersection(set(lst2))
# print(list(lst3))

# 38. Write a Python program to change the position of every n-th value with the (n+1)th in a list. 
# 	Sample list: [0,1,2,3,4,5]
# 	Expected Output: [1, 0, 3, 2, 5, 4]
# Sample= [0,1,2,3,43,5]
# for val in range(0,len(Sample)):
#         Sample[val],Sample[val+1]=Sample[val+1],Sample[val]

# print(Sample)

# 39. Write a Python program to convert a list of multiple integers into a single integer. 
# 		Sample list: [11, 33, 50]
# 		Expected Output: 113350
# sample=[11,33,50]
# a=""
# for val in sample:
#     a=str(a)+str(val)
# print(a) 

# 40. Write a Python program to split a list based on first character of word. 
# lst=["zniket","arshal","umit","rika","nuka"]
# for i in range(len(lst)):
#     for j in range(i+1,len(lst)):
#         if ord(i)<ord(j):
#             lst[i]=lst[j]
# print(lst)            




# l1=[3,4,2,7,8,9,1,5,6,4,2]
# for i in range(len(l1)):
#     for j in range(i+1,len(l1)):
#         if l1[i]>l1[j]:
#             l1[i],l1[j]=l1[j],l1[i]
# print(l1)


# 41. Write a Python program to create multiple lists.      

# 42. Write a Python program to find missing and additional values in two lists.      
# 	Sample data : Missing values in second list: b,a,c
# 	Additional values in second list: g,h
# 43. Write a Python program to split a list into different variables. 
lst=[1,3,44,55,666,77,88,99]

b=lst.split("33")
print(b)

# 44. Write a Python program to generate groups of five consecutive numbers in a list. 

# 45. Write a Python program to convert a pair of values into a sorted unique array. 

# 46. Write a Python program to select the odd items of a list. 

# 47. Write a Python program to insert an element before each element of a list.

# 48. Write a Python program to print a nested lists (each list on a new line) using the print() function. 

# 49. Write a Python program to convert list to list of dictionaries.
# Sample lists: ["Black", "Red", "Maroon", "Yellow"], ["#000000", "#FF0000", "#800000", "#FFFF00"]
# Expected Output: [{'color_name': 'Black', 'color_code': '#000000'}, {'color_name': 'Red', 'color_code': '#FF0000'}, {'color_name': 'Maroon', 'color_code': '#800000'}, {'color_name': 'Yellow', 'color_code': '#FFFF00'}]


# 50. Write a Python program to sort a list of nested dictionaries. 
# my_collection = {
# 						'KEY1':{'name':'foo','data':1351,'completed':100},
# 						'KEY2':{'name':'bar','data':1541,'completed':12},
# 						 'KEY3':{'name':'baz','data':58413,'completed':18}
# 					    }
# sorted_keys = sorted(my_collection, key=lambda x: (my_collection[x]['completed']))
# print(sorted_keys)
# 51. Write a Python program to split a list every Nth element. 
# 	Sample list: ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n']
# 	Expected Output: [['a', 'd', 'g', 'j', 'm'], ['b', 'e', 'h', 'k', 'n'], ['c', 'f', 'i', 'l']]


# 52. Write a Python program to compute the difference between two lists.      
# Sample data: ["red", "orange", "green", "blue", "white"], ["black", "yellow", "green", "blue"]
# Expected Output:
# 	Color1-Color2: ['white', 'orange', 'red']
# 	Color2-Color1: ['black', 'yellow']


# 53. Write a Python program to create a list with infinite elements. 

# 54. Write a Python program to concatenate elements of a list. 

# 55. Write a Python program to remove key values pairs from a list of dictionaries. 

# 56. Write a Python program to convert a string to a list. 

# 57. Write a Python program to check if all items of a given list of strings is equal to a given string. 

# 58. Write a Python program to replace the last element in a list with another list. 
# 	Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
# 	Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]


# 59. Write a Python program to check whether the n-th element exists in a given list. 

# 60. Write a Python program to find a tuple, the smallest second index value from a list of tuples.
# 61. Write a Python program to create a list of empty dictionaries. 

# 62. Write a Python program to print a list of space-separated elements.

# 63. Write a Python program to insert a given string at the beginning of all items in a list.
# 	Sample list : [1,2,3,4], string : emp
# 	Expected output : ['emp1', 'emp2', 'emp3', 'emp4']

# 64. Write a Python program to iterate over two lists simultaneously.

# 65. Write a Python program to move all zero digits to end of a given list of numbers. 
# 	Expected output:
# 	Original list:
# 	[3, 4, 0, 0, 0, 6, 2, 0, 6, 7, 6, 0, 0, 0, 9, 10, 7, 4, 4, 5, 3, 0, 0, 2, 9, 7, 1]
# 	Move all zero digits to end of the said list of numbers:
# 	[3, 4, 6, 2, 6, 7, 6, 9, 10, 7, 4, 4, 5, 3, 2, 9, 7, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# 66. Write a Python program to find the list in a list of lists whose sum of elements is the highest. 
# 	Sample lists: [1,2,3], [4,5,6], [10,11,12], [7,8,9]
# 	Expected Output: [10, 11, 12]

# 67. Write a Python program to find all the values in a list are greater than a specified number. 
# 68. Write a Python program to extend a list without append.      
# 	Sample data: [10, 20, 30]
# 	[40, 50, 60]
# 	Expected output : [40, 50, 60, 10, 20, 30]

# 69. Write a Python program to remove duplicates from a list of lists.      
# 		Sample list : [[10, 20], [40], [30, 56, 25], [10, 20], [33], [40]]
# 		New List : [[10, 20], [30, 56, 25], [33], [40]]

# 70. Write a Python program to find the items starts with specific character from a given list. 
# 		Expected Output:
# 		Original list:
# 		['abcd', 'abc', 'bcd', 'bkie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
# 		Items start with a from the said list:
# 		['abcd', 'abc', 'acjd']
# 		Items start with d from the said list:
# 		['dagfa']
# 		Items start with w from the said list:
# 		[]

# 71. Write a Python program to check whether all dictionaries in a list are empty or not. 
# 	Sample list : [{},{},{}]
# 	Return value : True
# 	Sample list : [{1,2},{},{}]
# 	Return value : False

# 72. Write a Python program to flatten a given nested list structure.
# 		Original list: [0, 10, [20, 30], 40, 50, [60, 70, 80], [90, 100, 110, 120]]
# 		Flatten list:
# 		[0, 10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
# 73. Write a Python program to remove consecutive duplicates of a given list. 
# 		Original list:
# 		[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# 		After removing consecutive duplicates:
# 		[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]

# 74. Write a Python program to pack consecutive duplicates of a given list elements into sublists.
# 	Original list:
# 	[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
# 	After packing consecutive duplicates of the said list elements into sublists:
# 	[[0, 0], [1], [2], [3], [4, 4], [5], [6, 6, 6], [7], [8], [9], [4, 4]]

# 75. Write a Python program to create a list reflecting the run-length encoding from a given list of integers or a given list of characters. 
# 	Original list:
# 	[1, 1, 2, 3, 4, 4.3, 5, 1]
# 	List reflecting the run-length encoding from the said list:
# 	[[2, 1], [1, 2], [1, 3], [1, 4], [1, 4.3], [1, 5], [1, 1]]
# 	Original String:
# 	automatically
# 	List reflecting the run-length encoding from the said string:
# 	[[1, 'a'], [1, 'u'], [1, 't'], [1, 'o'], [1, 'm'], [1, 'a'], [1, 't'], [1, 'i'], [1, 'c'], [1, 'a'], [2, 'l'], [1, 'y']]

# 76. Write a Python program to create a list reflecting the modified run-length encoding from a given list of integers or a given list of characters. 
# 	Original list:
# 	[1, 1, 2, 3, 4, 4, 5, 1]
# 	List reflecting the modified run-length encoding from the said list:
# 	[[2, 1], 2, 3, [2, 4], 5, 1]
# 	Original String:
# 	aabcddddadnss
# 	List reflecting the modified run-length encoding from the said string:
# 	[[2, 'a'], 'b', 'c', [4, 'd'], 'a', 'd', 'n', [2, 's']]

# 77. Write a Python program to decode a run-length encoded given list.
# 	Original encoded list:
# 	[[2, 1], 2, 3, [2, 4], 5, 1]
# 	Decode a run-length encoded said list:
# 	[1, 1, 2, 3, 4, 4, 5, 1]

# 78. Write a Python program to split a given list into two parts where the length of the first part of the list is given. 
# 	Original list:
# 	[1, 1, 2, 3, 4, 4, 5, 1]
# 	Length of the first part of the list: 3
# 	Splited the said list into two parts:
# 	([1, 1, 2], [3, 4, 4, 5, 1])

# 79. Write a Python program to remove the K'th element from a given list, print the new list. Original list:
# 	[1, 1, 2, 3, 4, 4, 5, 1]
# 	After removing an element at the kth position of the said list:
# 	[1, 1, 3, 4, 4, 5, 1]
# 80. Write a Python program to insert an element at a specified position into a given list. 
# 	Original list:
# 	[1, 1, 2, 3, 4, 4, 5, 1]
# 	After inserting an element at kth position in the said list:
# 	[1, 1, 12, 2, 3, 4, 4, 5, 1]

# 81. Write a Python program to extract a given number of randomly selected elements from a given list. 
# 	Original list:
# 	[1, 1, 2, 3, 4, 4, 5, 1]
# 	Selected 3 random numbers of the above list:
# 	[4, 4, 1]

# 82. Write a Python program to generate the combinations of n distinct objects taken from the elements of a given list. 
# HINT
# Original list: [1, 2, 3, 4, 5, 6, 7, 8, 9] Combinations of 2 distinct objects: [1, 2] [1, 3] [1, 4] [1, 5] .... [7, 8] [7, 9] [8, 9]

# 83. Write a Python program to round every number of a given list of numbers and print the total sum multiplied by the length of the list. 
# 	Original list: [22.4, 4.0, -16.22, -9.1, 11.0, -12.22, 14.2, -5.2, 17.5]
# 	Result:
# 	243
# 84. Write a Python program to round the numbers of a given list, print the minimum and maximum numbers and multiply the numbers by 5. Print the unique numbers in ascending order separated by space. 
# 	Original list: [22.4, 4.0, 16.22, 9.1, 11.0, 12.22, 14.2, 5.2, 17.5]
# 	Minimum value: 4
# 	Maximum value: 22
# 	Result:
# 	20 25 45 55 60 70 80 90 110

# 85. Write a Python program to create a multidimensional list (lists of lists) with zeros. 
# Multidimensional list: [[0, 0], [0, 0], [0, 0]]


# 86. Write a Python program to create a 3X3 grid with numbers.
# 	3X3 grid with numbers:
# 	[[1, 2, 3], [1, 2, 3], [1, 2, 3]]

# 87. Write a Python program to read a matrix from console and print the sum for each column. Accept matrix rows, columns and elements for each column separated with a space(for every row) as input from the user. 
# 	Input rows: 2
# 	Input columns: 2
# 	Input number of elements in a row (1, 2, 3):
# 	1 2
# 	3 4
# 	sum for each column:
# 	4 6

# 88. Write a Python program to read a square matrix from console and print the sum of matrix primary diagonal. Accept the size of the square matrix and elements for each column separated with a space (for every row) as input from the user. 
# 	Input the size of the matrix: 3
# 	2 3 4
# 	4 5 6
# 	3 4 7
# 	Sum of matrix primary diagonal:
# 	14

# 89. Write a Python program to Zip two given lists of lists. 
# 	Original lists:
# 	[[1, 3], [5, 7], [9, 11]]
# 	[[2, 4], [6, 8], [10, 12, 14]]
# 	Zipped list:
# 	[[1, 3, 2, 4], [5, 7, 6, 8], [9, 11, 10, 12, 14]]
# 90. Write a Python program to count number of lists in a given list of lists. 
# 		Original list:
# 		[[1, 3], [5, 7], [9, 11], [13, 15, 17]]
# 		Number of lists in said list of lists:
# 		4
# 		Original list:
# 		[[2, 4], [[6, 8], [4, 5, 8]], [10, 12, 14]]
# 		Number of lists in said list of lists:
# 		3

# 91. Write a Python program to find the list with maximum and minimum length. 
# 	Original list:
# 	[[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# 	List with maximum length of lists:
# 	(3, [13, 15, 17])
# 	List with minimum length of lists:
# 	(1, [0])
# 	Original list:
# 	[[0], [1, 3], [5, 7], [9, 11], [3, 5, 7]]
# 	List with maximum length of lists:
# 	(3, [3, 5, 7])
# 	List with minimum length of lists:
# 	(1, [0])
# 	Original list:
# 	[[12], [1, 3], [1, 34, 5, 7], [9, 11], [3, 5, 7]]
# 	List with maximum length of lists:
# 	(4, [1, 34, 5, 7])
# 	List with minimum length of lists:
# 	(1, [12])

# 92. Write a Python program to check if a nested list is a subset of another nested list. 
# 		Original list:
# 		[[1, 3], [5, 7], [9, 11], [13, 15, 17]]
# 		[[1, 3], [13, 15, 17]]
# 		If the one of the said list is a subset of another.:
# 		True
# 		Original list:
# 		[[[1, 2], [2, 3]], [[3, 4], [5, 6]]]
# 		[[[3, 4], [5, 6]]]
# 		If the one of the said list is a subset of another.:
# 		True
# 		Original list:
# 		[[[1, 2], [2, 3]], [[3, 4], [5, 7]]]
# 		[[[3, 4], [5, 6]]]
# 		If the one of the said list is a subset of another.:
# 		False

# 93. Write a Python program to count the number of sublists contain a particular element. 
# 		Original list:
# 		[[1, 3], [5, 7], [1, 11], [1, 15, 7]]
# 		Count 1 in the said list:
# 		3
# 		Count 7 in the said list:
# 		2
# 		Original list:
# 		[['A', 'B'], ['A', 'C'], ['A', 'D', 'E'], ['B', 'C', 'D']]
# 		Count 'A' in the said list:
# 		3
# 		Count 'E' in the said list:
# 		1

# 94. Write a Python program to count number of unique sublists within a given list. 
# 	Original list:
# 	[[1, 3], [5, 7], [1, 3], [13, 15, 17], [5, 7], [9, 11]]
# 	Number of unique lists of the said list:
# 	{(1, 3): 2, (5, 7): 2, (13, 15, 17): 1, (9, 11): 1}
# 	Original list:
# 	[['green', 'orange'], ['black'], ['green', 'orange'], ['white']]
# 	Number of unique lists of the said list:
# 	{('green', 'orange'): 2, ('black',): 1, ('white',): 1}

# 95. Write a Python program to sort each sublist of strings in a given list of lists. 
# 	Original list:
# 	[[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
# 	Sort the list of lists by length and value:
# 	[[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]

# 96. Write a Python program to sort a given list of lists by length and value. 
# 	Original list:
# 	[[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
# 	Sort the list of lists by length and value:
# 	[[0], [2], [0, 7], [1, 3], [9, 11], [13, 15, 17]]

# 97. Write a Python program to remove sublists from a given list of lists, which contains an element outside a given range. 
# 	Original list:
# 	[[2], [0], [1, 2, 3], [0, 1, 2, 3, 6, 7], [9, 11], [13, 14, 15, 17]]
# 	After removing sublists from a given list of lists, which contains an element outside the given range:
# 	[[13, 14, 15, 17]]

# 98. Write a Python program to scramble the letters of string in a given list. 
# 	Original list:
# 	['Python', 'list', 'exercises', 'practice', 'solution']
# 	After scrambling the letters of the strings of the said list:
# 	['tnPhyo', 'tlis', 'ecrsseiex', 'ccpitear', 'noiltuos']

# 99. Write a Python program to find the maximum and minimum values in a given heterogeneous list. 
# 	Original list:
# 	['Python', 3, 2, 4, 5, 'version']
# 	Maximum and Minimum values in the said list:
# 	(5, 2)

# 100. Write a Python program to extract common index elements from more than one given list. 
# 	Original lists:
# 	[1, 1, 3, 4, 5, 6, 7]
# 	[0, 1, 2, 3, 4, 5, 7]
# 	[0, 1, 2, 3, 4, 5, 7]
# 	Common index elements of the said lists:
# 	[1, 7]