# def fizzbuzz(number): 
#     if number%3==0 and number%5==0:
#         return "FizzBuzz"   
#     elif number%3==0:
#         return "Fizz"
#     elif number%5==0:
#         return "Buzz"
#     else:
#         return number
# p=fizzbuzz(15)      
# print(p)

# x = 1 + 2 * 3 - 8 / 4
# print(x)

# x=(1,2,3,4,5)
# print("Hello World")

# print(max(x))

# def stuff():
#     print('Hello')
#     return
#     print('World')

# # stuff()
# tot = 0 
# for i in [5, 4, 3, 2, 1] :
#     tot = tot + 1
#     print(tot)
# print(tot)\\

zork = 0
for thing in [9, 41, 12, 3, 74, 15] :
    zork = zork + thing
print('After', zork)

arr=(12,3,4,5)
x=8
for val in arr:
    if len(arr)>2:
        if val == x:
            print(arr.index(val))
    else:
        print(0)