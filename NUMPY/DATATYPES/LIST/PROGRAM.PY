# list1=[1,2,3,4,"rs",1+2j,2.5]
# print(type(list1))

# list1[0]="sanika"
# print(list1)

# list1[0:3]=[10,20,30]
# print(list1)

# print(list1[0:4])    #-1

# print(list1[-1:-4:-1]) #+1


# list2=[]            #empty list
# print(len(list2))

# print(id(list1))    #1677737300160
# list1[0]=99
# print(list1,id(list1))   #1677737300160


# a='python'
# print(type(a))          #str into list
# b=list(a)
# print(type(b))

# a=1+2j
# print(type(a))          #complex into list
# b=list([a])
# print(type(b))


# a=2.5  
# print(type(a))          #float into list
# b=list([a])
# print(type(b))

# a=True
# print(type(a))          #boolean into list
# b=list([a])
# print(type(b))


# #pre defined data type
# 1.append
# list1=[1,3,5,7,9,'sakshi']
# lst=[20,30,40]
# list1.append("sanika")
# print(list1)

# list1.append(lst)
# print(list1)

# list1.append(20,30,40,50)       #error
# print(list1)

# 2.insert
# list1=[10,20,30,40,50,60,70,80]
# list1.insert(2,20)
# print(list1)

# list1.insert(200,20)
# print(list1)

# list1.insert(-200,20)
# print(list1)


# # 3.clear
# list1=[10,20,30,40,50,60,70,80]
# list1.clear()
# print(list1)

# # 4.remove
# list1=[10,20,30,40,50,60,70,80]
# list1.remove(20)
# print(list1)

# 5.pop(index)
# list1=[10,20,30,40,50,60,70,80]
# list1.pop(2)
# print(list1)

# # 6.pop
# list1=[10,20,30,40,50,60,70,80]
# list1.pop()
# # print(list1)

# # 7.del operator
# list1=[10,20,30,40,50,60,70,80]
# del list1[4]
# print(list1)

# del list1[0:4]
# print(list1)

# 8.index
# list1=[10,20,30,40,50,60,70,80]
# print(list1.index(40))

#enumerate:value and  index
# list1=[10,20,30,40,50,60,70,80]
# for i,v in enumerate(list1):
#     print(i,"---->",v)

# for a in list1:
#     print(a)

# 9.copy()
# a.shallow copy
# lst1=[10,"RS"]

# print(lst1,id(lst1))  # 2743929376960
# lst2=lst1.copy() # Shallow Copy

# print(lst2,id(lst2))  

# lst1.append("Python")
# lst2.insert(1,23.45)
# print(lst1,id(lst1))
# print(lst2,id(lst2))

# 10.count()
# list2=[10,20,30,40,50,30,60,70,80]
# print(list2.count(30))


# 11.reverse
# list1=[10,3,4,50,60,7]
# list1.reverse()
# print(list1)


# 12.sort
# list1=[10,3,4,50,60,7]
# list1.sort()
# print(list1)

# list1.sort(reverse=True)
# print(list1)

# list1.sort(reverse=False)
# print(list1)

# 13.extend
# list1=[10,3,4,50,60,7]
# list2=[56,67]
# list1.extend(list2)
# print(list1)

# list1.append(list2)
# print(list1)


list1=[12,3,4,5,6,7,72,[23,45,56],[34,56,78,79]]
print(list1[7][1])

list1[7].append(10)
print(list1)

del list1[7][1]
print(list1)