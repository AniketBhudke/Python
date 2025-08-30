# number1=int("Enter The First Number:")
# number2=int("Enter The Second Number:")
# print("Sum OF two Number:",number1+number2)

# n=int(input("Enter The First Number:"))
# sum=0
# if n>0:
#     while n>0:
#         r=n%10
#         sum=sum+r
#         n=n//10
# print(sum)    


st=True
t1=(1,2,3,4,1,5)
for i in range(len(t1)):
    if t1.count(t1[i])>2:
        