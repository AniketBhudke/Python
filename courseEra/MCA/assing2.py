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
#         print(i)    


# n=int(input("Enter A Number:"))
# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print(j,end="")
#     print()


# n=int(input("Enter A Number:"))
# a=1
# for i in range(a,n+1,1):
#     for j in range(1,i,2):
#         print(j,end="")
#     print()

n = int(input("Enter n: "))

for i in range(1, n + 1):
    # Increasing part
    for j in range(1, i + 1):
        print(j, end=" ")
    # Decreasing part
    for j in range(i - 1, 0, -1):
        print(j, end=" ")
    print()
