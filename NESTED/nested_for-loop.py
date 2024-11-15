# #simple nested while loop program
# for i in range(1,6):
#     # print(i)
#     for j in range(1,4):
#         print(i,j)
#     else:    
#         print("-----------------------") 
# else:          
#     print("------outer for loop---------")     

#simle program but in reerse direction
# for i in range(5,0,-1):
#     for j in range(3,0,-1):
#         print(i,j)
#     else:
#         print("--------------------")
# else:
#     print("------outer for loop---------")     

#simple inner nested program(3 loop)
# for i in range(1,5):
#     for j in range(1,3):
#         for k in range(1,4):
#             print(i,j,k)
#         else:
#             print("---inner nested loop-----")   
#     else:
#         print("-----Innner Loop-----")
# else:
#     print("----Outer For Loop------")                

#table 
# n=int(input("Enter a Number:"))
# for i in range(1,n):
#     for j in range(1,11):
#         print("{} * {} = {}".format(i,j,i*j))
#     else:
#         print("-------------------------------")
# else:
#     print("----Outer else block of for loop-----------")     
# 
# 1. Accessing Elements in a Nested List
# nested_list = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
#Question: How would you access the number 80 from this nested list?       
# l = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
# print(l[-1][1])

#Modify an Element in a Nested List
#nested_list = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
#Question: Change the value 50 to 55.
l=[[10, 20, 30], [40, 50, 60], [70, 80, 90]]
# l[1][1]=55
# print(l)
# for sublist in l:
#     for element in sublist:
#         if element==50:
#             element=55
#             l.append(element)
# print(l)            



#nested_list = [[1, 2], [3, 4, 5], [6]]
#Question: Write a Python program that calculates the sum of all the elements in this nested list.
# s=0
# nested= [[1, 2], [3, 4, 5], [6]]
# for sublist in nested:
#     for element in sublist:
#         print(element)
#         s=s+element
# print(s)        

#4. Find Maximum Value in a Nested List
#nested_list = [[5, 3, 9], [1, 6, 7], [2, 8, 4]]
#uestion: Write a Python program to find the maximum value in this nested list.
# nested= [[5, 3, 9], [1, 6, 7], [2, 8, 4]]
# maximum=2
# for sublist in nested:
#     for element in sublist:
#         if element>maximum:
#             maximum=element
# print(maximum)            

# Flatten a Nested List
#nested_list = [[1, 2], [3, 4], [5, 6]]
#Question: Write a Python program to flatten this nested list into a single list. The output should be:
#[1, 2, 3, 4, 5, 6]
# nested= [[1, 2], [3, 4], [5, 6]]
# n=[]
# for sublist in nested:
#     for element in sublist:
#         n.append(element)
# print(n)        