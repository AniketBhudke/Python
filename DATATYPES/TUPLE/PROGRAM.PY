#in tuple only two predefined function available count and index

# tuple1=(1,23,45,56,60,5)

# tuple1[0]=9
# print(tuple1)  #TypeError: 'tuple' object does not support item assignment

# print(tuple1[::-1])

# print(tuple1.index(45))


# print(tuple1.count(45))

# t2=sorted(tuple1)
# print(t2,type(t2))

# t3=tuple(t2)
# print(t3,type(t3))

#nested tuple 
# nested=(1,3,4,5,[23,45,675,6],34,56,[67,3,4,56])
# print(nested[4].remove(23))
# print(nested)

tuple1=(1,23,45,56,60,5)
tpl=(1,2,3,4,5)

print(id(tuple1))
x=sorted(tuple1)
print(x)

print(x[3])
tuple1=tuple(x)
print(id(tuple1))


print(tpl[2])









#pre-defined function

#isdisjoint
# s1={10,20,30,40}
# s2={50,60,70}
# s3=s1.isdisjoint(s2)  #match=True   notMatch=false
# print(s3)

#issuperset
# s1={10,20,30,40}
# s2={40}
# s3=s1.issuperset(s2)  #() jo ya bracket mde lihala tya che srva ch element dusrya set mde present asel tr=True,otherwise=false
# print(s3)

#issubset
# s1={40}
# s2={40,50}
# s3=s1.issubset(s2)  #. chya pahile jo set aaahe tya mdle srv value ()ya mdlya set mde asel tr=True,otherwise false
# print(s3)

#union
# s1={10,20,30,40}
# s2={50,60,70}
# s3=s1.union(s2)  #combine krun dete
# print(s3)

#intersection
# s1={10,20,30,40}
# s2={50,60,70,40}
# s3=s1.intersection(s2)  #common vlaue dete
# print(s3)

# #difference:-duplicate value remove krte aani .chya aadhi cha set return krte(1 set output)
# s1={10,20,30,90,40}
# s2={50,90}
# s3=s1.difference(s2)  #doni madale common element remove krte aani first set output dete
# print(s3)  #{40, 10, 20, 30}
# s4=s2.difference(s1)
# print(s4)  #{50}

#symmetric_difference:-print kelya nntr doni set mdlya unique value return krte(2 set output)
# s1={10,20,30,90,40}
# s2={50,90}
# s3=s1.symmetric_difference(s2)  #doni madale common element remove krte aani doni combine krun unique value return krte
# print(s3)  #{40, 10, 50, 20, 30}
# s4=s2.symmetric_difference(s1)
# print(s4)  #{50, 20, 40, 10, 30}

#difference_update
# s1={10,20,30,40}
# s2={40,50,60}
# s3=s1.difference_update(s2)  #pahilya ch ya mde return krto
# print(s1)  #{10, 20, 30}

# #symmetric_difference_update
# s1={10,20,30,40}
# s2={40,50,60}
# s3=s1.symmetric_difference_update(s2)
# print(s1)  #{10, 50, 20, 60, 30}

#update
# s1={10,20,30,40}
# s2={40,50,60}
# s3=s1.symmetric_difference_update(s2) #update return unique value in first set(before . set)
# print(s1)