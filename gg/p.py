# #15-12-2024
# # Given an array, arr of n integers, and an integer element x, find whether element x is present in the array. Return the index of the first occurrence of x in the array, or -1 if it doesn't exist.

# # Examples:

# # Input: arr[] = [1, 2, 3, 4], x = 3
# # Output: 2
# # Explanation: There is one test case with array as [1, 2, 3 4] and element to be searched as 3. Since 3 is present at index 2, the output is 2.
# # Input: arr[] = [10, 8, 30, 4, 5], x = 5
# # Output: 4
# # Explanation: For array [1, 2, 3, 4, 5], the element to be searched is 5 and it is at index 4. So, the output is 4.
# # Input: arr[] = [10, 8, 30], x = 6
# # Output: -1
# # Explanation: The element to be searched is 6 and its not present, so we return -1.

# # class Solution:
# #     #Complete the below function
# #     def search(self,arr, x):
# #         #Your code here
# #         for val in arr:
# #             if val == x:
# #                 return arr.index(x)
# #         else:
# #             return -1


# # Given two arrays: a[] and b[], where both arrays may contain duplicate elements. The task is to determine whether array b is a subset of array a. It's important to note that both arrays can be unsorted. Additionally, each occurrence of a duplicate element within an array is considered as a separate element of the set.

# # Examples:

# # Input: a[] = [11, 7, 1, 13, 21, 3, 7, 3], b[] = [11, 3, 7, 1, 7]
# # Output: Yes
# # Explanation: b[] is a subset of a[]
# # Input: a[] = [1, 2, 3, 4, 4, 5, 6], b[] = [1, 2, 4]
# # Output: Yes
# # Explanation: b[] is a subset of a[]
# # Input: a[] = [10, 5, 2, 23, 19], b[] = [19, 5, 3]
# # Output: No
# # Explanation: b[] is not a subset of a[]
# # a=[12,3,4,5,6,7,8,9]
# # b=[3,4,5,6]
       
# # a=set(a)
# # b=set(b)
# # # Your code here
# # res=b.issubset(a)
# # print(res)

# # a="aniket"
# # print(a[::-1])

# # Given two arrays arr1 and arr2 of equal size, the task is to find whether the given arrays are equal. Two arrays are said to be equal if both contain the same set of elements, arrangements (or permutations) of elements may be different though.
# # Note: If there are repetitions, then counts of repeated elements must also be the same for two arrays to be equal.

# # Examples:

# # Input: arr1[] = [1, 2, 5, 4, 0], arr2[] = [2, 4, 5, 0, 1]
# # Output: true
# # Explanation: Both the array can be rearranged to [0,1,2,4,5]
# # Input: arr1[] = [1, 2, 5], arr2[] = [2, 4, 15]
# # Output: false
# # Explanation: arr1[] and arr2[] have only one common value.

# # arr1=[1,35,565,77,77,9]
# # arr2=[35,1,565,9,77]
# # for val in arr1:
# #     if val in arr2:
# #         res=True
# #     else:
# #         res=False
# # print(res)          


# # Given an array arr of positive integers. Reverse every sub-array group of size k.

# # Note: If at any instance, k is greater or equal to the array size, then reverse the entire array. You shouldn't return any array, modify the given array in place.

# # Examples:

# # Input: k = 3, arr= [1, 2, 3, 4, 5]
# # Output: [3, 2, 1, 5, 4]
# # Explanation: First group consists of elements 1, 2, 3. Second group consists of 4,5.
# # Input: k = 5, arr = [5, 6, 8, 9]
# # Output: [9, 8, 6, 5]
# # Explnation: Since k is greater than array size, the entire array is reversed.

# # def subArrayReverse(arr,k):
# #     arr1=[]
# #     for i in range(k,-1,-1):
# #         arr1.append(arr[i])
# #     for j in range(len(arr)-1,k-1,-1):
# #         arr1.append(arr[j])
# #     return arr1        

# #               #4
# # a=[2,4,55,66,7,8,90,20]   #
# # k=len(a)//2
# # res=subArrayReverse(a,k)  
# # print(res) 



# # Given an array arr, rotate the array by one position in clock-wise direction.

# # Examples:

# # Input: arr = [1, 2, 3, 4, 5]
# # Output: [5, 1, 2, 3, 4]
# # Explanation: If we rotate arr by one position in clockwise 5 come to the front and remaining those are shifted to the end.
# # Input: arr = [9, 8, 7, 6, 4, 2, 1, 3]
# # Output: [3, 9, 8, 7, 6, 4, 2, 1]
# # Explanation: After rotating clock-wise 3 comes in first position.

# # def solution(arr):
# #     arr1=[]
# #     arr1.insert(0,arr[-1])
# #     for i in range(0,len(arr)-1,1):
# #         arr1.append(arr[i])
# #     return arr1    

# # arr=[4,5,7,8,90,5,8,9,00,78,99,90,55]
# # res=solution(arr)
# # print(res) 

# #date=04-02-2024
# # def findpalindrome():
# #     arr=[11,12,13,14,15,16]
# #     count=0
# #     for val in arr:
# #         if str(val)==str(val)[::-1]:
# #             count=count+1
# #         else:
# #             return False
# #     else:
# #         if count==len(arr):
# #             return True   
# # findpalindrome()         

# # #date-05-02-2024

# # def reverseInGroups( arr, k):
# #         if k>len(arr):
# #             return arr[::-1]
# #         else:
# #             new_lst=[]
# #             for i in range(0,k):
# #                  new_lst.append(arr[i])
# #             for i in range(-1,k-1):
# #                  new_lst.append(arr[i])     
# #             return new_lst  


# # arr,k=[1,2,3,4,5],3

# # for i in range(0, len(arr), k):
# #     arr[i:i+k] = arr[i:i+k][::-1]  # Reverse the subarray from index i to i+k
# # print(arr)

# #date=07-03-2024
# # def insertAtIndex( arr, sizeOfArray, ind, element):
# #         #Your code here
# #         b=[]
# #         if sizeOfArray>ind:
# #             for value in arr:
# #                 if arr.index(value)==ind: 
# #                      b.append(element)
# #                 else:
# #                      b.append(value)     
# #         return b   


# # arr=[1,2,3,4,5]
# # sizeOfArray=5
# # ind=2   #ya index vr element kara lgte
# # element=10
# # res=insertAtIndex(arr,sizeOfArray,ind,element)
# # print(res)

# #date-08-02-2024
# # def longest(self, arr):
# #         # code here
# #         long=""
# #         for word in arr:
# #             if len(word)>len(long):
# #                 long=word
# #         return long        
            
# # arr=["abc","def","ghi","jkl","mno"]
# # res=longest(arr)
# # print(res)

# #date-09-02-2024
# # class Solution:
# #     def lastIndex(self, s: str) -> int:
# #         # code here
# #         ind=s.rfind("1")
# #         return ind    
# #         return -1
            
# # def getOddOccurrence(arr, n):
# #         # code here 
# #         for i in range(len(arr)):
# #             cont=arr.count(arr[i])
# #             if cont%2!=0:
# #                   return arr[i]
            

# # arr={1,2,3,2,4,4,1,3,5,6,7,6,7}
# # n=13
# # res=getOddOccurrence(arr,n)
# # print(res)

# #date-12-02-2024
# #me
# # def arraySum( arr):
# #     s=0
# #     for value in arr:
# #         s+=value
# #     print(s)
   	

# # arr=[1,2,3,4,5]    
# # arraySum(arr)    

# # #chatGPT
# # def arraySum( arr):
# #     s = sum([value for value in arr])
# #     print(s)

# # arr=[1,2,3,4,5]    
# # arraySum(arr)    

# # import pandas as pd

# # lst=["Rossum","Travis","Ritche","Dennis","Hunter"]
# # s=pd.Series(lst,name="Emp")
# # print("Series Object Data")
# # print(s,type(s))

# # import numpy as np
# # import pandas as pd
# # lst=["Rossum","Travis","Ritche","Dennis","Hunter","James","Jhon"]
# # s=pd.Series(lst)
# # print("Series Object Data")
# # print(s)

# # print(s[0::2])

# # print(s[0])

# # s[[0,1]]=["VAN","OLI"]
# # print(s)



# # #15-02-2024
# # def min_value_to_balance(arr):
# #         # code here
# #         ind=len(arr)//2
# #         s1,s2=0,0
# #         for i in range(0,ind):
# #             s1=arr[i]+s1
# #         for i in range(ind,len(arr)):
# #             s2=arr[i]+s2
# #         if s1>s2:
# #             return s1-s2
# #         return s2-s1 

# # s=min_value_to_balance([1,2,3,4,5,6])
# # print(s)

# # #16-02-2024
# # def countOddEven(arr):
# # 		#Code here
# #     odd=0
# #     even=0
# #     for value in arr:
# #         if value%2==0:
# #             even=even+1
# #         else:
# #             odd=odd+1
# #     return odd,even  
# # arr=[1,2,3,4,5,6]
# # s=countOddEven(arr)
# # print(s)

# # def prime():
# #     s=int(input("Enter:"))
# #     res="prime"
# #     for i in range (2,s):
# #         if s%i==0:
# #             res="not prime"
# #     return res     
# # res=prime()
# # print(res)    

# # def findElements(arr):
# #         # Your code goes here
# #         lst=[]
# #         arr.sort()
# #         for i in range(len(arr)-2):
# #             lst.append(arr[i])
# #         return lst    
        
# # res=findElements([11,3,4,5,6,9])
# # print(res)


# # def findSum(arr):
# # 		# code here
# # 	lst=[]
# # 	s=0
# # 	for val in arr:
# # 		if val not in lst:
# # 			lst.append(val)
# # 			s=s+val
# # 	return s
# #     #return sum(set(arr))
				
# # res=findSum([1,2,3,4,4,5,6,7,8,8,9])
# # print(res)

# # def majorityWins(arr, n, x, y):
# #         # code here
# #         countx=arr.count(x)
# #         county=arr.count(y)
# #         if countx>county:
# #             return x
# #         elif   countx<county:  
# #             return y
# #         elif countx==county:
# #             if x>y:
# #                 return y
# #             else:
# #                 return x
    
# # res=majorityWins([1,1, 2, 2,3,3, 4,6],5,1,2)
# # print(res)

# # arr=[11,22,33,44,55,66,77]
# # num1=22
# # num2=44
# # ind2 = len(arr) - 1 - arr[::-1].index(num2)
# # print(ind2)
        

# # import pandas as pd

# # df=pd.DataFrame({"Days":["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
# #                  "Week1":[27,29,32,33,33,31,29],
# #                  "Week2":[29,30,31,33,34,34,31],
# #                  "Week3":[29,28,25,27,31,30,29]})
# # print(df)
# # df.to_csv("abcd.csv")

# # def valueEqualToIndex(arr):
# #         lst=[]
# #         for i in range(len(arr)):
# #             if arr[i]==i+1:
# #                 lst.append(arr[i])
# #         return lst        
# # res=valueEqualToIndex([10,2,3,5,7])    
# # print(res)



# # l1 = [7,871,7687,867,86786,786,7867]
# # print(f"Before sorting : {l1}")
# # for i in range(len(l1)):
# #         for j in range(i+1,len(l1)):
# #                 if l1[i]>l1[j]:
# #                         l1[i],l1[j]=l1[j],l1[i]
# # print(f"After sorting : {l1}")


# # Fibonacci series
# # n1,n2=0,1
# # n=10
# # print(f"Fibonacci Series: {n1} {n2} = ",end=' ')
# # for i in range(n):
# #     n3=n1+n2
# #     print(n3,end=' ')
# #     n1=n2
# #     n2=n3

# # 0+1=1
# # 1+1=2 
# # 
# # 
# # 
# # 
# # 
# # 
# # 
# # 
# # 
# # 
# # 
# # 
# # #


# # arr=[1,2,3,4,5]
# # d=2
# # lst=[]
# # lst=arr[d:]+arr[:d]
# # print(lst)  # Output: [2, 3, 4, 5,

# # for i in range(d):
# #         first_element = arr.pop(0)
# #         arr.append(first_element)
# # print(arr)

# # def oneLinePrintEle():        
# #         arr=[1,2,3,4,5,6]
# #         for i in range(len(arr)):
# #              print(arr[i],end="")
# # oneLinePrintEle()        

# #replace 0 to 5
# # n=7090
# # lst=list(str(n))
# # for i in range(len(lst)):
# #     if lst[i]=="0":
# #         lst[i]='5'
# # print("".join(lst))    

# # num=7090
# # result = 0
# # place = 1
    
# # while num > 0:
# #         digit = num % 10  # last degit aanala 
        
# #         if digit == 0:# Replace 0 with 5
# #             digit = 5  
        
# #         result =result+ digit * place #4
# #         place =place * 10
# #         num //= 10  # Remove the last digit
# # print(result)        
      

# # n=6
# # lst=[]
# # lst.append(n)
# # while n==1:
# #     if n%2==0:
# #         lst.append(n//2)
# #         n=lst[-1]
# #     else:
# #         lst.append(n*3+1)
# #         n=lst[-1]
# # print(lst)            


# # n=5
# # b=bin(n)
# # print(b)
# # lst=list(str(b))
# # print(lst)
# # for i in range(len(lst)):
# #     if lst[i]=='0':
# #         lst[i]='1'
# #     else:
# #         lst[i]='0'
# # print("".join(lst))     
# # 



# # from collections import Counter
# # arr=[11,22,33,44,55,11,22,33]
# # count=Counter(arr)
# # for val in arr:
# #     if count[val]==1:
# #         print(val)


# # arr1=[1,3,5,6,8]
# # arr2=[3,5,6,3,4]
# # count=0
# # for i in range(len(arr1)):
# #     for j in range(len(arr2)):
# #         if arr1[i]+arr2[j]==10:
# #             count=count+1
# # print(count)

# # target=6
# # nums=[1,2,3,4,5,6,722,4,5]
# # print(sum(nums))        

# # lst=[12,11,44,67,8,9]
# # lst1=[]
# # s=[]
# # for val in lst:
# #     lst1=list(str(val))
# #     for val1 in lst1:
# #         if val1 not in s:
# #             s.append(val1)
# # print(" ".join(s))            


# # a=[1,2,5,6]
# # for a[-1] in a:
# #     print(a[-1])

# # a,b='20'
# # b,c='68'
# # print(a+b+c)

# # a=[1,2,5,6]
# # for i in a:
# #     a.remove(i)
# # print(a)    



# # a=[1,2,5,6]
# # for i in a:
# #     a.remove(i)
# # print(a)    


# # from sys import argv
# # print(argv)

# t,v=[1,2,33]
# print(t,v)




# # def val():
# #     return int(input("Enter A Value:"))

# # def calculation(a):
# #     def square():
# #         n=a()
# #         res=n**2
# #         return n,res
# #     return square

# # res=calculation(val)()
# # print(type(res))
# # print(res[0],res[1])
# #--------------------------------------------------------------------------------------------

# # def kvr():
# #     return input("Enter A value:")

# # res=kvr()
# # print(type(res))
# #-----------------------------------------------------------------------------------------------

# # def square(bang):
# #     def squareval():
# #         n=bang()
# #         s_val=n**2
# #         return n,s_val
# #     return squareval

# # @square
# # def getval():
# #     return int(input("Enter A Value:"))

# # n,s_val=getval()
# # print(s_val)
# #----------------------------------------------------------------------------------------------

# # def cuberoot(bang):
# #     def cuberootval():
# #         n,s_val,c_val=bang()
# #         c_r_val=n**0.5
# #         return n,s_val,c_val,c_r_val
# #     return cuberootval

# # def cube(hyd):
# #     def cubeval():
# #         n,s_val=hyd()
# #         c_val=n**3
# #         return n,s_val,c_val
# #     return cubeval

# # def square(kvr):
# #     def squareval():
# #         n=kvr()
# #         s_val=n**2
# #         return n,s_val
# #     return squareval

# # @cuberoot
# # @cube
# # @square
# # def getval():
# #     return int(input("Enter A Value:"))

# # n,s_val,c_val,c_r_val=getval()
# # print(f"Square={s_val}")
# # print(f"Cube={c_val}")
# # print(f"Cube Root={c_r_val}")


# a=[1,2,3,4,5,67,8]

a,b,c={"one":1,"two":2,"three":3}
print(a,b,c)