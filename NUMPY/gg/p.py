#15-12-2024
# Given an array, arr of n integers, and an integer element x, find whether element x is present in the array. Return the index of the first occurrence of x in the array, or -1 if it doesn't exist.

# Examples:

# Input: arr[] = [1, 2, 3, 4], x = 3
# Output: 2
# Explanation: There is one test case with array as [1, 2, 3 4] and element to be searched as 3. Since 3 is present at index 2, the output is 2.
# Input: arr[] = [10, 8, 30, 4, 5], x = 5
# Output: 4
# Explanation: For array [1, 2, 3, 4, 5], the element to be searched is 5 and it is at index 4. So, the output is 4.
# Input: arr[] = [10, 8, 30], x = 6
# Output: -1
# Explanation: The element to be searched is 6 and its not present, so we return -1.

# class Solution:
#     #Complete the below function
#     def search(self,arr, x):
#         #Your code here
#         for val in arr:
#             if val == x:
#                 return arr.index(x)
#         else:
#             return -1


# Given two arrays: a[] and b[], where both arrays may contain duplicate elements. The task is to determine whether array b is a subset of array a. It's important to note that both arrays can be unsorted. Additionally, each occurrence of a duplicate element within an array is considered as a separate element of the set.

# Examples:

# Input: a[] = [11, 7, 1, 13, 21, 3, 7, 3], b[] = [11, 3, 7, 1, 7]
# Output: Yes
# Explanation: b[] is a subset of a[]
# Input: a[] = [1, 2, 3, 4, 4, 5, 6], b[] = [1, 2, 4]
# Output: Yes
# Explanation: b[] is a subset of a[]
# Input: a[] = [10, 5, 2, 23, 19], b[] = [19, 5, 3]
# Output: No
# Explanation: b[] is not a subset of a[]
# a=[12,3,4,5,6,7,8,9]
# b=[3,4,5,6]
       
# a=set(a)
# b=set(b)
# # Your code here
# res=b.issubset(a)
# print(res)

# a="aniket"
# print(a[::-1])

# Given two arrays arr1 and arr2 of equal size, the task is to find whether the given arrays are equal. Two arrays are said to be equal if both contain the same set of elements, arrangements (or permutations) of elements may be different though.
# Note: If there are repetitions, then counts of repeated elements must also be the same for two arrays to be equal.

# Examples:

# Input: arr1[] = [1, 2, 5, 4, 0], arr2[] = [2, 4, 5, 0, 1]
# Output: true
# Explanation: Both the array can be rearranged to [0,1,2,4,5]
# Input: arr1[] = [1, 2, 5], arr2[] = [2, 4, 15]
# Output: false
# Explanation: arr1[] and arr2[] have only one common value.

# arr1=[1,35,565,77,77,9]
# arr2=[35,1,565,9,77]
# for val in arr1:
#     if val in arr2:
#         res=True
#     else:
#         res=False
# print(res)          


# Given an array arr of positive integers. Reverse every sub-array group of size k.

# Note: If at any instance, k is greater or equal to the array size, then reverse the entire array. You shouldn't return any array, modify the given array in place.

# Examples:

# Input: k = 3, arr= [1, 2, 3, 4, 5]
# Output: [3, 2, 1, 5, 4]
# Explanation: First group consists of elements 1, 2, 3. Second group consists of 4,5.
# Input: k = 5, arr = [5, 6, 8, 9]
# Output: [9, 8, 6, 5]
# Explnation: Since k is greater than array size, the entire array is reversed.

# def subArrayReverse(arr,k):
#     arr1=[]
#     for i in range(k,-1,-1):
#         arr1.append(arr[i])
#     for j in range(len(arr)-1,k-1,-1):
#         arr1.append(arr[j])
#     return arr1        

#               #4
# a=[2,4,55,66,7,8,90,20]   #
# k=len(a)//2
# res=subArrayReverse(a,k)  
# print(res) 



# Given an array arr, rotate the array by one position in clock-wise direction.

# Examples:

# Input: arr = [1, 2, 3, 4, 5]
# Output: [5, 1, 2, 3, 4]
# Explanation: If we rotate arr by one position in clockwise 5 come to the front and remaining those are shifted to the end.
# Input: arr = [9, 8, 7, 6, 4, 2, 1, 3]
# Output: [3, 9, 8, 7, 6, 4, 2, 1]
# Explanation: After rotating clock-wise 3 comes in first position.

# def solution(arr):
#     arr1=[]
#     arr1.insert(0,arr[-1])
#     for i in range(0,len(arr)-1,1):
#         arr1.append(arr[i])
#     return arr1    

# arr=[4,5,7,8,90,5,8,9,00,78,99,90,55]
# res=solution(arr)
# print(res) 

#date=04-02-2024
# def findpalindrome():
#     arr=[11,12,13,14,15,16]
#     count=0
#     for val in arr:
#         if str(val)==str(val)[::-1]:
#             count=count+1
#         else:
#             return False
#     else:
#         if count==len(arr):
#             return True   
# findpalindrome()         

# #date-05-02-2024

# def reverseInGroups( arr, k):
#         if k>len(arr):
#             return arr[::-1]
#         else:
#             new_lst=[]
#             for i in range(0,k):
#                  new_lst.append(arr[i])
#             for i in range(-1,k-1):
#                  new_lst.append(arr[i])     
#             return new_lst  


# arr,k=[1,2,3,4,5],3

# for i in range(0, len(arr), k):
#     arr[i:i+k] = arr[i:i+k][::-1]  # Reverse the subarray from index i to i+k
# print(arr)

#date=07-03-2024
# def insertAtIndex( arr, sizeOfArray, ind, element):
#         #Your code here
#         b=[]
#         if sizeOfArray>ind:
#             for value in arr:
#                 if arr.index(value)==ind: 
#                      b.append(element)
#                 else:
#                      b.append(value)     
#         return b   


# arr=[1,2,3,4,5]
# sizeOfArray=5
# ind=2   #ya index vr element kara lgte
# element=10
# res=insertAtIndex(arr,sizeOfArray,ind,element)
# print(res)

#date-08-02-2024
# def longest(self, arr):
#         # code here
#         long=""
#         for word in arr:
#             if len(word)>len(long):
#                 long=word
#         return long        
            
# arr=["abc","def","ghi","jkl","mno"]
# res=longest(arr)
# print(res)

#date-09-02-2024
# class Solution:
#     def lastIndex(self, s: str) -> int:
#         # code here
#         ind=s.rfind("1")
#         return ind    
#         return -1

arr=[11,22,33,44,55,66]
num1=22
num2=55
ind1=arr.index(num1)
print(ind1)


x=r.normal(loc=4,scale=55,size=(4,5))
print(x)