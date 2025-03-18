#bitwise AND
# a=5
# b=99
# print(a&b)#------------odd number asla tr 1 output dete
# number = 7
# print( number & 1)
# if number & 1:  # If LSB is 1, number is odd
#     print(f"{number} is odd")
# else:
#     print(f"{number} is even")

#bitwise OR
# a=5
# b=3
# print(a|b)

#bitwise XOR
# a=0
# b=1
# print(a^b)

# a={1:2,3:5}
# i=1
# s=0
# s=s+a[i]
# print(s)

a=[11,2,33,44,55,34,5,6,7,8]
even=[]
odd=[]
for i in range(len(a)):
    if a[i]%2==0:
        even.append(a[i])
    else:
        odd.append(a[i])    
even.sort()
odd.sort()
a.clear()
a=even+odd
for i in range(len(a)):
    print(a[i],end="  ")
