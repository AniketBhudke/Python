#1234=10
# n=int(input("Enter A number:"))
# s=0
# if n>0:
#     while n>0:
#         r=n%10
#         s=s+r
#         n=n//10
# print(s)

# n=int(input("Enter The number:"))
# s="It IS Not Prime Number"
# for i in range(2,n+1):
#     if n%i!=0:
#         s="It Is Prime Number"
#     break
# print(s)        

#fibonacci series
# n=int(input("Enter A Number:"))
# ini_num=0
# sec_num=1
# for i in range(1,n+1):
#     sum_two=ini_num+sec_num
#     print(ini_num,sec_num)
#     ini_num=sec_num
#     sec_num=sum_two

#8626 = 8+6+2+6=22  2+2=4
# addition=0
# n=int(input("Enter A Number:"))
# while n>0:
#     r=n%10
#     addition=addition+r
#     n=n//10
# print(addition)
# add=0
# while addition>0:
#     r=addition%10
#     add=add+r
#     addition=addition//10
# print(add)

# n=int(input("Enter A Number:"))
# s="It is Prime"
# for i in range(2,n+1):
#     for j in range(2,i):
#         if i%j!=0:
#             s="It is not Prime"
# print(s)

import sys

def fizzbuzz(a):
    if a % 15 == 0:
        return "FizzBuzz"
    if a % 3 == 0:
        return "Fizz"
    if a % 5 == 0:
        return "Buzz"
    return str(a)

data = sys.stdin.read().strip().split()
if not data:
    sys.exit()

nums = list(map(int, data))

# If first number equals the count of remaining numbers, treat it as T
if len(nums) > 1 and nums[0] == len(nums) - 1:
    arr = nums[1:]
else:
    # Otherwise treat every number in input as a testcase (covers single input too)
    arr = nums

results = [fizzbuzz(a) for a in arr]
print("\n".join(results))
