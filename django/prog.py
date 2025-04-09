#command line argument 

# import sys
# print(sys.argv)


#some example
t=(10,15,20)
x,_,y=t
print(x,_,y) #output: 10 20

a=1_2
print(a*2)

x,y=4,3
print((x--x)+(y--y))

print(pow(2,7,5))


n=6
while n>0:
    print(n)
    n-=2 if n%3==0 else 1
    
lst=[11,'bool',54,{},33,[],""]
print(list(filter(bool,lst)))   

i=[1,0,2,0,3,0]
for val in i:
    if val ==0:
        i.remove(val)
        i.append(val)
print(i)        \\\


i=[1,0,2,0,3,0]
for val in i:
    if val ==0:
        i.remove(val)
        i.append(val)
print(i)        