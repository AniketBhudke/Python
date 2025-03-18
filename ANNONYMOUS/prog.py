# addop=lambda a,b:a+b
# res=addop(100,200)
# print(res)

# addop=lambda a,b:"a is  greater" if a>b else "b is greater"
# res=addop(5100,200)
# print(res)

# findbig=lambda a,b,c:a if a>b and a>c  else b if b>a and b>c else c

# res=findbig(10,20,30)
# print(res)  # Output: 30

#filter
# lst=[1,2,3,4,5,6,-1,-1,-3,-4,-5,-8]
# pos=[]
# neg=[]
# poslist=lambda val:pos.append(val) if val>0 else neg.append(val)
# res=list(map(poslist,lst)) 
# print(pos,neg)

# lst=[1,2,3,4,5,6,-1,-1,-3,-4,-5,-8]
# poslist=lambda val:val+6
# res=list(filter(poslist,lst)) 
# print(res)

#map

# lst=[1,2,3,4,5,6,-1,-1,-3,-4,-5,-8]
# poslist=lambda val:val+6
# res=list(map(poslist,lst)) 
# print(res)

import functools
#reduce

# lst1=[10,20,30,40,50,60]
# poslist=lambda a,b:a+b
# res=functools.reduce(poslist,lst1) 
# print(res)


# def val():
#     return int(input("Enter A Value:"))

# def calculation(a):
#     def square():
#         n=a()
#         res=n**2
#         return n,res
#     return square

# res=calculation(val)()
# print(type(res))
# print(res[0],res[1])



# def kvr():
#     return input("Enter A value:")

# res=kvr()
# print(type(res))


# def square(bang):
#     def squareval():
#         n=bang()
#         s_val=n**2
#         return n,s_val
#     return squareval

# @square
# def getval():
#     return int(input("Enter A Value:"))

# n,s_val=getval()
# print(s_val)

def cuberoot(bang):
    def cuberootval():
        n,s_val,c_val=bang()
        c_r_val=n**0.5
        return n,s_val,c_val,c_r_val
    return cuberootval

def cube(hyd):
    def cubeval():
        n,s_val=hyd()
        c_val=n**3
        return n,s_val,c_val
    return cubeval

def square(kvr):
    def squareval():
        n=kvr()
        s_val=n**2
        return n,s_val
    return squareval

@cuberoot
@cube
@square
def getval():
    return int(input("Enter A Value:"))

n,s_val,c_val,c_r_val=getval()
print(f"Square={s_val}")
print(f"Cube={c_val}")
print(f"Cube Root={c_r_val}")