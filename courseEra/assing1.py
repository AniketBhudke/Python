#sum of two number
num1=int(input("Enter 1st Number:"))
num2=int(input("Enter 2nd Number:"))
print("Sum Of Two Number:",num1+num2)

print(70*"-")
num1=int(input("Enter 1st Number:"))
num2=int(input("Enter 2nd Number:"))
if num1>num2:
    print(num1,"is Greater")
else:
    print(num2,"ids greater")

num1=int(input("Enter 1st Number:"))
num2=int(input("Enter 2nd Number:"))
if num1>num2:
    print(num1,"is Greater")
elif num2>num1:
    print(num2,"is greater")
else:
    print("Both Are Equal")
print(70*"-")

    
num1=int(input("Enter 1st Number:"))
num2=int(input("Enter 2nd Number:"))
num3=int(input("Enter 3rd Number:"))
if num1>num2 and num1>num3:
    print(num1,"is Greater")
elif num2>num1 and num2>num3:
    print(num2,"is greater")
elif num3>num1 and num3>num2:
    print(num3,"Is Greater")
else:
    print("three are equal")
print(70*"-")

num1=int(input("Enter 1st Number:"))
for i in range(1,num1+1):
    print(i)
print(70*"-")


num1=int(input("Enter 1st Number:"))
for i in range(1,num1+1):
    if i%2==0:
        print(i)
print(70*"-")


num1=int(input("Enter 1st Number:"))
for i in range(1,num1+1):
    if i%2!=0:
        print(i)
print(70*"-")

num1=int(input("Enter 1st Number:"))
s=0
for i in range(1,num1+1):
    s=s+i
print(s)
print(70*"-")

print(70*"-")
num1=int(input("Enter 1st Number:"))
for i in range(1,num1+1):
    if num1%i==0:
        print(i)
print(70*"-")

num1=int(input("Enter 1st Number:"))
for i in range(num1,-num1,-1):
    print(i)
    
print(70*"-")