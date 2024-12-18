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

def solution():
`````       and                 `

arr=[4,5,7,8,90,55]
res=solution()


