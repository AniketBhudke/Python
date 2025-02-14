# #Program for Generating 1 to N Numbers where N is +VE
# # n=int(input("Enter a number:"))
# # for i in range(n):
# #     print(i)

# #Program for Generating N to 1 where N is +VE
# # n=int(input("Enter a number:"))
# # for i in range(n,0,-1):
# #     print(i)

# #Program for generating Mul table for Number n.
# # number=int(input("enter a number:"))
# # for i in range(1,11,1):
# #     print(i*number)

# #Program for finding Sum of N Natural Numbers
# # s=0
# # n=int(input("Enter a natural number limit:"))
# # for i in range(1,n+1,1):
# #     print(i)
# #     s=s+i
# # print(s)    

# # Program for finding Sum of N Natural Numbers and their squares also
# # n=int(input("enter a number:"))
# # s=0
# # ss=0
# # c=0
# # for i in range(1,n+1,1):
# #     print(i)
# #     ss=ss+i*i
# #     c=c+i*i*i
# #     s=s+i
# # print(ss,s,c)    

# #Program for finding Product of N Natural Numbers
# # n=int(input("enter a number:"))
# # p=1
# # for i in range(1,n+1,1):
# #     print(i)
# #     p=p*i
# # print(p)    

# # #enter 10 number from user and find out Even or Odd
# # n=int(input("enter a numnber:"))
# # for i in range(1,n,1):
# #     if i%2==0:
# #         print()

# # #Reverse a String
# # s="sagar"
# # for i in range(len(s)-1,-1,-1):
# #     print(s[i])

# # # Factorial Calculation
# num=int(input("Enter a number:"))
# for i in range(num,1,-1):
#     print(num[i]*num[i-1])
# # #  Find the Largest Number

# num=int(input("Enter Any Number:"))
# #num=2389
# s=0
# count=0
# tn=num # We are pre-serving the Original number in temp Var tn
# while(num>0):
#     d=num%10     #2389
#     s=s+d        #0+9
#     num=num//10  #2389//10=2380
#     count=count+1
# print("sum of Digits({})={}".format(tn,s))
# print(count)


# print(2389//10)


# num=int(input("Enter Any Number:"))
# if(num<=0):
#     print("{} is invalid input".format(num))
# else:
#     s=0
#     for d in str(num):
#         s=s+int(d)
#     else:
#         print("sum of digits({})={}".format(num,s))

#prime number
#armstrong number

# num=int(input("enter a number: ")) #123
# count=0
# while (num>=0):
#     count=count+1
#     print(count)    

# user_number=int(input("enter a number:"))
# number=10
# while (user_number!=number):
#     print("you are number matching :")
    
# 2.Write a program to print sum of
# digits of input number    

# s=0
# num=int(input("enter a number:"))
# while(num>0):
#     m=num%10   #
#     s=s+m
#     num=num//10
# print(s)      

#123=321 integer number reverse
# reverse_num=0
# num=int(input("enter a number:"))  #6021
# while(num>0):
#     r=num%10   
#     reverse_num = (reverse_num*10) + r
#     num=num//10
# print(reverse_num)    

#prime number 


# num=int(input("enter a number:"))
# if (num%num==0 and num%1==0) and num%2==0 or num%3==0:
#     print("it is not prime number")
# elif (num%num==0 and num%1==0) and num%2!=0 and num%3!=0 :
#     print("it is prime number:")






# print("Sum : ",sum(l1:=list(range(1,11,1))),"List : ",l1)

#sum average max min 
# lst1=[10,2,3,4,5]
# s=0
# count=0
# for i in lst1:
#     s=s+i
#     count=count+1
# print(s,count)
# avg=s/count
# print(avg)    

# list1=[]
# min = 0
# for i in range(len(list1)):  #3
#     if len(list1)==0:
#         print("list is empty:")
#     elif list1[i] < min:   #12 > 0
#         min = list1[i]
        
#                #max=12
# print(f"min : {min}")


# s=0
# for i in range(5,51,5):
#     print(i)

#     if i%2!=0:
#         s+=i
# print("sum of add numbers in digit is:",s)

# s="PYTHON"
# for ch in s: # s="PYTHON"
#     if(ch=="T") or (ch=="O"):
#         continue
#     print("{}".format(ch),end='')

# s="PYTHON"
# i=0
# while(i<len(s)): # s="PYTHON"
#    if(s[i]=="T"):
#        i = i + 1  #skip trr krte pn toh increment zala pahije puda che item print kryala 
#        continue
#    print("{}".format(s[i]),end="")
#    i = i + 1   #while loop increment


# s="python"
# for ch in s:
#     if ch in ['a','e','i','o','u']:
#         break
#     print(ch)


# num=int(input("enter a number:"))
# res="is a prime number"
# for i in range(2,num):     (1,51)
#     if num%i==0:
#         res="is not a prime number"

# print(num,res)        


#insert the element in empty list and also set the limit that how many element are added in a list

#find the even number prime number between 1 to 50 and 

# for i in range(1,51,1):
#     if i%2==0:
#         for j in range(1,50,1):
#             res="it is a prime number"
#             prime=j%i
#             if prime:
#                 res="it is not prime num"
#         print(prime)
# print(res)        

# for i in range(1,51,1):
#     for j in range(1,51,1):
#         res="it is prime number"
#         if i%j==0:
#             res="it is not prime number"
#             print(i%j) 
#             continue       

# Print all numbers from 1 to 20 using a for loop.
#by for loop
# for i in range(1,21,1):
#     print(i)

#by while loop
# i=1
# while(i<=20):
#     print(i)
#     i=i+1

# Print all the elements in a list: fruits = ['apple', 'banana', 'cherry'].

#by for loop
# fruits = ['apple', 'banana', 'cherry']
# for fruit in fruits:
#     print(fruit)

#by while loop
# i=0
# fruits = ['apple', 'banana', 'cherry']
# while(i<=len(fruits)-1):
#     print(fruits[i])
#     i=i+1

# Print all characters in the string "Hello, World!".

#while loop
# str="Hello, World!"
# i=0
# while(i<len(str)):
#     print(str[i])
#     i=i+1


#by for 
# str="Hello, World!"
# for ch in str:
#     print(ch)

# Calculate the sum of all numbers from 1 to 100 using a for loop.
# i=1
# s=0
# while(i<=100):
#     s=s+i
#     print(i)
#     i=i+1
# print(s)    

# s=0
# for i in range(1,101,1):
#     s=s+i
#     print(i)
# print(s)    

# Find the product of all numbers from 1 to 10 using a for loop.
# p=1
# for i in range(1,10,1):
#     p=p*i
# print("product",p)

# i=1
# p=1
# while(i<=10):
#     p=p*i
#     i=i+1
# print(p)


# Print only the even numbers between 1 and 50 using a for loop.

# for i in range(1,51,1):
#     if i%2==0:
#         print(i)

# i=1
# while(i<=50):
#     if i%2==0:
#         print(i)  
#     i=i+1          

# Print only the odd numbers between 1 and 50 using a for loop.
# for i in range(1,51,1):
#     if i%2!=0:
#         print(i)

# i=1
# while(i<=50):
#     if i%2!=0:
#         print(i)  
#     i=i+1          

# Print the square of each number from 1 to 10 using a for loop.

# for i in range(1,10,1):
#     print("i * i =",i*i)

# i=1
# while(i<=10):
#     print("i * i=",i*i)
#     i=i+1

# Print the cube of each number from 1 to 5 using a for loop.
# for i in range(6):
#     print("i * i * i=",i*i*i)

# i=1
# while(i<=5):
#     print("i * i * i= ",i*i*i)
#     i=i+1

# Iterate through a list of integers and print the sum of even numbers.
# s=0
# lst=[1,2,3,4,5,6,7,8,9,10]
# for i in lst:
#     if i%2==0:
#         s=s+i
# print(s)

# Iterate through a list of integers and print the sum of odd numbers.
# lst=[11,12,13,14,15,16,17,18,19]
# sum=0
# for i in lst:
#     if i%2==0:
#         sum=sum+i
# print(sum)    


# Print each element of the list animals = ['cat', 'dog', 'rabbit', 'bird'] and its length.
# animals = ['cat', 'dog', 'rabbit', 'bird']
# for i in animals:
#     print(i)

# Print each number in a range from 10 to 1 in reverse order.
# for i in range(10,1,-1):
#     print(i)

# Find the maximum number in a list: numbers = [4, 2, 9, 1, 5, 6].
# numbers = [4, 2, 9, 1, 5, 6]
# big=2
# for i in numbers:
#     if i>=big:
#         big=i
# print(big) 

# numbers=[4, 2, 9, 1, 5, 6]
# big=numbers[0]
# i=1
# while(i < len(numbers)):
#     if numbers[i] > big:
#         big=numbers[i]
#     i=i+1
# print(big)

# Find the minimum number in a list: numbers = [7, 3, 8, 2, 10, 1].
# numbers = [7, 3, 8, 2, 10, 1]
# min=7
# for i in numbers:
#     if i <= min:
#         min=i
# print(min)        

# numbers = [7, 3, 8, 2, 10, 1]
# min=2
# i=1
# while(i<len(numbers)):
#     if numbers[i]<=min:
#         min=numbers[i]
#     i=i+1
# print(min)        

# Create a list of squares of numbers from 1 to 10 using a for loop.
# sqr=[]
# for i in range(1,11,1):
#     num_sqr=i*i
#     sqr.append(num_sqr)
# print(sqr) 
   
# Count how many times a number appears in a list: numbers = [1, 3, 4, 1, 2, 1, 5].
# numbers = [1, 3, 4, 1, 2, 1, 5]
# count=0
# i=1
# while(i<=len(numbers)):
#     count=count+1
#     i=i+1
# print(count)    

# Write a for loop that prints all elements of a 2D list: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]].
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i in range(len(matrix)): #3
#     for j in range(len(matrix)): #3
#         print(matrix[i][j],end=' ')
#     print()

# Print the multiplication table of a given number using a for loop.
# number=int(input("Enter a number:"))
# for i in range(1,11,1):
#     print(f"{number} * {i} = {number*i}")

# Iterate through a list of strings and print only the strings that start with the letter 'a'.
# lst=["aniket","sagar","prathamesh","harshal","kunal"]
# for i in lst:
#     if i[0]=='a':
#         print(i)

# Intermediate Level:
# Print the first 10 Fibonacci numbers using a for loop.


# Find the factorial of a given number using a for loop.
# n=int(input("enter a number for Factor : "))
# fact=1
# for i in range(n,0,-1):
#     fact=fact*i
#     continue
# print(fact)

# Write a for loop that reverses a given string.
# s="python"
# for i in s[::-1]:
#     print(i,end="")

# Write a for loop to check if a given number is prime.
# num=int(input("enter a number:"))
# if (num<0):
#     print("it is invalid input")
# else:
#     res=True
#     for i in range(2,num,1):
#         if num%i==0:
#             res=False
#             break      
#     result="it is prime number"if res else "it is not prime"
#     print(result)

# Iterate through a dictionary and print the keys and values: person = {'name': 'John', 'age': 25, 'city': 'New York'}
# person = {'name': 'John', 'age': 25, 'city': 'New York'}
# for k,v in person.items():
#     print(k,v)
# for i in person:
#     print(i,person[i])

# Write a for loop to count how many vowels are in a given string.
# s="pythoooon"
# vowels=0
# for ch in s:
#     if ('a' in ch) or ('e' in ch) or ('i' in ch) or ('o' in ch) or ('u' in ch):
#         vowels=vowels+1
# print(vowels)        
    

# Print the index and value of each element in the list: colors = ['red', 'green', 'blue'].
# colors = ['red', 'green', 'blue']
# for key,items in enumerate(colors):
#     print(key,items)

# Write a for loop that prints the first 10 multiples of a number.

# count=0
# number=int(input("enter a number:"))
# for i in range(1,100,1):
#     if number%i==0:
#         print(i)
#         if count==10:
#             break
#         count=count+1
# print(count)


# Write a for loop to find the length of each word in a sentence.
# a="kunal is a topper of your class"
# lst=a.split()
# print(lst)
# for ch in lst:
#     print(f"{ch} lenghth of chractor ={len(ch)}")

# Flatten a list of lists using a for loop: nested_list = [[1, 2], [3, 4], [5, 6]].
# a=[]
# nested_list = [[1, 2], [3, 4], [5, 6]]
# for i in nested_list:
#     for j in i:
#         a.append(j)
# print(a)
    
# Count how many words in a list have more than 4 letters.
# lst=["aniket","ann","dip",1,2,3,"ska","shrikant","kunal","harsh"]
# for words in lst:
#     if type(words)==str:
#         if len(words)>=4:
#             print(words)

# Iterate through two lists simultaneously and print their elements: list1 = [1, 2, 3], list2 = ['a', 'b', 'c'].
# list1 = [1, 2, 3]
# list2 = ['a', 'b', 'c']
# for i in range(0,len(list1)):
#     print(list1[i],list2[i])                

# Write a for loop to sum the diagonal elements of a matrix: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]].
# s=0
# matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i in matrix:
#     for j in i:
#         s=s+j
# print(s)        


# Write a for loop that prints the cumulative sum of numbers in a list: numbers = [1, 2, 3, 4].
# numbers = [1, 2, 3, 4]
# s=0
# for num in numbers:
#     s=s+num
# print(s)    


# Find the second largest number in a list using a for loop.
##logic 1
# second_large=2
# lst=[12,1,23,45,78,9,7,8]
# max1 = max(lst)
# for num in lst:   
#     if max1>num>second_large:  
#         second_large=num 
# print(second_large)       

##logic2
# max=1
# second_large=2
# lst=[12,1,23,45,78,9,7,8]
# for num in lst:
#     if num>=max:
#         max=num

# lst.remove(max)
# print(lst)        

# second_large=1 
# for num in lst:
#     if num>=second_large:
#         second_large=num
# print(second_large)


# Write a for loop to merge two lists element-wise: list1 = [1, 2, 3], list2 = [4, 5, 6].
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]

# lst=[]
# for i in range(0,len(list1)):
#     lst.append(list1[i])
#     lst.append(list2[i])
# print(lst)

# Write a for loop to generate a pattern of stars (*), increasing in size:
# markdown
# Copy code
# *
# **
# ***
# ****

# Print all elements of a list but skip the element 'banana': fruits = ['apple', 'banana', 'cherry'].
# fruits = ['apple', 'banana', 'cherry']
# for element in fruits:
#     if element != 'banana':
#         print(element)

# Write a for loop that calculates the average of numbers in a list.
# lst=[1,2,12,13,14,15,14,4,44]
# count=0
# sum=0
# for ele in lst:
#     count=count+1
#     sum=sum+ele
# print(count,sum) 
# print(f"Average of {sum} number ={sum//count}")   

# Write a for loop to count how many elements in a list are divisible by 3.
# lst=[1,11,12,13,14,15,16,17,88,45]
# count=0
# for element in lst:
#     if element%3==0:
#         count=count+1
# print(count)        

# Write a for loop that prints only the unique elements of a list: numbers = [1, 2, 2, 3, 4, 4, 5].
numbers = [1, 2, 2, 3, 4, 4, 5]
lst=[]
for i in numbers:
    for j in numbers:
        print(j+1)
        
    
# Advanced Level:
# Write a for loop to transpose a matrix: matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]].
# Write a for loop that iterates over a list and removes duplicates.
# Write a for loop to rotate elements of a list: list1 = [1, 2, 3, 4], rotating it to [4, 1, 2, 3].
# Write a for loop to find the most frequent element in a list.
# Create a dictionary from two lists using a for loop: keys = ['a', 'b', 'c'], values = [1, 2, 3].
# Write a for loop to check if two lists are the same (element-wise).
# Write a for loop that prints the common elements between two lists.
# Write a for loop to implement bubble sort on a list.
# Write a for loop to perform matrix multiplication on two matrices.

#print even digit of a given number
# number=int(input("Enter a number:"))
# while(number>0):
#     r=number%10
#     if r%2==0:
#         print(r)
#     number=number//10
    
#print odd digit of a given number
# number=int(input("Enter a number:"))
# while(number>0):
#     r=number%10
#     if r%2!=0:
#         print(r)
#     number=number//10    

#reverse of int without using extend and slicing
# reverse_num=0
# number=int(input("enter a number: "))
# while(number > 0):
#     r=number%10
#     reverse_num=(reverse_num*10) + r 
#     number=number//10
# print(reverse_num)    

#will get uppercase & lowercase letter separately
# str=input("Enter a string: ")
# lowercase=[]
# uppercase=[]
# for ch in str:
#     if ch.isupper()==True:
#         uppercase.append(ch)
#     else:
#         lowercase.append(ch) 
# print(uppercase)
# print(lowercase)          


#which will accept a line of text and display only vowels question incomplete

#which will accept a line of text and display only special symbol hint:alphanum
# str=input("Enter a string: ")
# for ch in str:
#     if ch.isalnum()==False:
#         print(ch)

#accept a line of text and display only alphabhet hint:isalpha
# str=input("Enter a string: ")
# for ch in str:
#     if ch.isalpha()==True:
#         print(ch)

#accept a line of text and get those words whose len(ranges) 2 to 3
# str=input("Enter a string: ")
# for i in range(2,4,1):
#     print(str[i])

#python is oop lang
# str="python is oop lang"
# x=str.split()
# print(x)
# for i in range(len(x)):
#     print(x[i])
#     for j in x[i]:
#         print(j)
    





