# # # # #string
# # # # #type casting

# # # str1="python"

# # # # print(str1[6:0:-1])
# # # # print(str1[-2:3:1])

# # # # print(str1.index("p"))
# # # # print(str1.count("p"))
# # # # print(str1.capitalize())
# # # # print(str1.find("t",0,6))

# # # print(tuple(str1))
# # # print(list(str1))
# # # print(set(str1))
# # # print(bool(str1))
# # # # print(complex(str1))
# # # # print(int(str1))
# # # # print(float(str1))
# # # # print(bytes(str1))
# # # # print(bytearray(str1))
# # # # print(dict(str1))
# # # # print(range(str1))
# # # st="abc"
# # # print(frozenset(st))

# # # list1={1:"abc"}
# # # print(str(list1))
# # # print(type(str(list1)))

# # # # print([1,2,3,4] >>[12,23,4,45])

# # # # str1="PYTHON"
# # # # print(str1[::2][::-1])
# # # r = range(1, 5)
# # # print(r)  # Output: 'range(1, 5)'


# # #LIST
# list1=[12,13,14,15,16,[12,13,14],"sagar",1.2]
# print(list1[-3][::-1])
# print(list1)



# # for i in list1:
# #     print(i,type(i))
# # print(id(list1))
# # list1[0]=123
# # print(list1)    
# # print(id(list1))
# # list1[-3].reverse()
# # print(list1)

# # list1.insert(-3,20)
# # print(list1)

# # list1.append(455)
# # print(list1)

# # list1[6]=2344
# # print(list1)

# # list1=[12,13,14,15,16,[12,13,14],"sagar",1.2]
# # list1[5].remove(13)
# # print(list1)

# # list1[5].pop()
# # print(list1)
# Create a list of 5 random numbers. How do you access the first and last element of the list?

# lst=[1,2,3,4,5]
# print(lst[0])
# print(lst[::1][0],lst[::1][-1])

# Add an element to the end of a list and remove an element from the list.
# lst1=[12,13,14,15,16]
# lst1.append(23)
# print(lst1)

# lst1=[12,13,14,15,16]
# lst1[-1]=224
# print(lst1)

    
# Check if the number 7 is present in the list. If it is, print its index.
lst1=[12,13,14,15,16,7]

# for i in lst1:
#     if 7 in lst1:
#         print(lst1.index(7))
#         break
#     else:
#         print("element not present")
#         break    

# Reverse the order of elements in the list without using the built-in reverse() function.

# print(lst1[::-1])
# print(lst1[len(lst1)::-1])

# Sort the list in ascending and descending order.
# lst1=[12,13,14,15,16,7]
# print(lst1)

# lst1.sort(reverse=False)
# print(lst1)

# lst1.sort(reverse=True)
# print(lst1)


# List Operations:
# Write a program to count the number of even and odd numbers in a list.
# lst1=[12,13,14,15,16,7]
# odd_count=0
# even_count=0
# for i in lst1:
#     if i%2==0:
#         even_count=even_count+1
#     else:
#         odd_count=odd_count+1    
# print(odd_count)
# print(even_count)

# Find the largest and smallest number in a list.
lst1=[12,13,14,15,16,7]
small=[]
large=[]

# lst1.sort()
# print(lst1)  

# small.append(lst1[0])
# print(small)      

# large.append(lst1[-1])
# print(large)      

# lst1=[12,13,14,15,16,7]
# small=[]
# large=[]

          

# lst1=[12,13,14,15,16,7]
# for i in lst1:
#     print(lst1)
#     if i>i[]:
#         large.append(i)

#     else:
#         small.append(i+1)    
# print(large)
# print(small)        

# How do you remove duplicates from a list?
# lst=[12,13,14,12,15]
# print(lst[0])
# print(lst[1])

# for i in lst:
#     print()
    # if lst[ls] 
    # print(lst[0] + lst[i+1])

# set1=set(lst)
# print(set1)

# lst1=list(set1)
# print(lst1)



# Write a Python program that combines two lists and removes duplicate values.
# lst=[12,13,14,12,15]
# lst1=[13,24,14,15]

# comb=lst+ lst1

# conrt_set=set(comb)

# lst1=list(conrt_set)
# print(lst1)

# Given a list of strings, create a new list containing only strings that start with the letter 'a'.
# list_str=["harshal","sagar","abc","kunal",12,13]
# only_str=[]

# for str in list_str:
#     if 
    

# List Comprehensions:
# Create a list of squares of all numbers from 1 to 10 using list comprehension.
# Given a list of numbers, create a new list with only the even numbers using list comprehension.
# Using list comprehension, generate a list of the first 10 multiples of 3.
# Write a list comprehension that creates a new list from an existing list, converting all negative numbers to their absolute values.
# List and Functions:
# Write a function that takes a list as input and returns the sum of all elements in the list.
# Write a function that returns the second largest element in a list.
# Create a function that checks if a list is a palindrome (reads the same forwards and backwards).
# Write a function that returns the index of the minimum element in a list.
# Write a function that removes all instances of a given value from a list.
# Advanced List Manipulation:
# Given a list of integers, rotate the list to the right by n positions.
# How do you flatten a list of lists (e.g., [[1, 2], [3, 4]] becomes [1, 2, 3, 4])?
# Write a program that counts the frequency of each element in a list.
# Given two lists of numbers, find the common elements between them.
# Create a list of tuples, where each tuple contains a number and its square, for all numbers from 1 to 5.
# Problem-Solving with Lists:
# Given a list of grades, write a program that calculates the average grade and prints the grades above the average.
