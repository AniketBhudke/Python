# # dict1={"python":"rossum","skc":67,"booklet":789,"quiz":789}
# # print(dict1)

# # dict1["python"]="jb"
# # print(dict1)

# # d1={10.2:23,10.1:234,10:89}
# # print(d1)

# # print(dict1["python"])

# # for index,value in enumerate(dict1):
# #     print(index,"-->",value)

# # # pre-defined datatype

# # # 1.clear()
# # dict1.clear()
# # print(dict1)

# # # 2.pop
# # dict2={1:"one",2:"two",3:"three",4:"four"}
# # dict2.pop(1)
# # print(dict2)

# # # 3.popitem
# # dict2.popitem()
# # print(dict2)

# # # 4. copy()

# # d2=dict2.copy()
# # print(d2)


# # # 5. get()--Most Imp

# # d3=dict2.get(2)
# # print(d3)

# # # 6. keys()

# # dic2={1:"one",2:"two",3:"three",4:"four"}
# # ks=dic2.keys()

# # for v in ks:
# #     print(v)



# # # 7. values()

# # dict2={1:"one",2:"two",3:"three",4:"four"}
# # val=dic2.values()

# # for v in val:
# #     print(v)



# # # 8. items()

# # kv=dic2.items()

# # for v in kv:
# #     print(v)



# d1={"one":1,"two":2,"three":3}
# print(d1)

# d1["one"]
# print(d1["one"])


# # predefined function
# # 1.keys

# for key in d1.keys():
#     print(key)

# # 2.values
# for val in d1.values():
#     print(val)

# # 3.items
# for k,v in d1.items():
#     print(k,v)

# #4.copy-------shallow copy
# d2=d1.copy()
# print(d2)    

# # 5.clear
# d1.clear()
# print(d1)

# # 6.pop()
# d2.pop("one")
# print(d2)

# #7.popitems
# d2.popitem()
# print(d2)

# # 8.get
# d2={"one":1,"two":2,"three":3}
# dict1=d2.get("one")
# print(dict1)

# for key,val in enumerate(d2):
#     print(key,"-----",val,d2[val])



d1={11:"one",12:"two",13:"three",14:"four"}
d1[0]="hvcfqy"
print(d1)

d1[11]="uhdyfd"
print(d1)

# d1.clear()
# print(d1)

d1.pop(12)
print(d1)

d2=d1.copy()
print(d2)

d2.popitem()
print(d2)

val=d2.get(13)
print(val)

ks=d1.keys()
print(ks)

vs=d1.values()
print(vs) 