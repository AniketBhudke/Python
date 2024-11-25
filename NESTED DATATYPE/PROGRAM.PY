# dict
# ------------
# dict in dict---Possible

# d1={1:"one",2:"two",3:"three",6:{4:"four",5:"five"}}
# print(d1[6])

# # print(d1.keys(4))

# d1[6][76767]="four"
# print(d1)

# d1[6].pop(5)
# print(d1)


# list in dict---Possible

# d1={1:"one",2:"three",3:"three",4:[12,23,45,6,7]}

# d1[4][1]=677
# print(d1)

# d1[4].append(4555)
# print(d1)

# d1[4].pop()
# print(d1)

# d1[4].pop(2)
# print(d1)

# tuple in dict--Possible
# d1={1:"one",2:"two",3:"three",4:(12,23,44,56,78)}

# g=d1[4].index(23)
# print(g)

# f=d1[4].count(23)
# print(f)


# d1[4]=555
# print(d1)

# set in dict---possible
1
# d={1:"one",2:"two",3:"three",4:{12,23,44,56,78}}

# # d[4][3]=888
# # print(d)

# d[4].add(234)
# print(d)

# d[4].remove(23)
# print(d)

# d[4].pop()
# print(d)

# ---------------------
# List
# ---------------------
# list in list---Possible
# lst1=[12,13,14,15,16,[12,34,56,78]]

# lst1[5].remove(12)
# print(lst1)


# lst1[5].append(12)
# print(lst1)


# lst1[5].pop(1)
# print(lst1)

# lst1[5][1]=77777
# print(lst1)


# tuple in list---Possible
# lst1=[12,13,14,15,16,(12,34,56,78)]
# print(lst1)

# lst=lst1[5].count(34)
# print(lst)



# set in list-----Possible
# lst1=[12,13,14,15,16,{12,34,56,78}]

# lst1[5].add(45)
# print(lst1)

# lst1[5].remove(45)
# print(lst1)

# dict in list-----Possible

# lst1=[12,13,14,15,16,8,{1:"one",2:"two"}]

# lst1[6][3]="nishant"
# print(lst1)

# --------------------------------------
# tuple
# --------------------------------------
# tuple in tuple---Possible
# tpl1=(1,2,3,4,5,(12,13,14,15))
# print(tpl1)

# t2=tpl1[5].count(12)
# print(t2)

# t2=tpl1[5].index(12)
# print(t2)

# list in tuple---Possible
# t2=(11,12,13,314,15,16,[17,18,19,20],22)
# print(t2)

# t2[6].append(35)
# print(t2)

# t2[6].remove(18)
# print(t2)

# t2[6].pop()
# print(t2)

# t2[6].pop(2)
# print(t2)

# set in tuple--Possible
# tpl=(12,13,14,15,{1245,1345,144,1,4})
# print(tpl)

# tpl[4].add(345)
# print(tpl)

# tpl[4].remove(345)
# print(tpl)

# tpl[4].pop()
# print(tpl)



# dict in tuple---Possible

# tpl=(12,13,14,15,16,17,{1:"one",2:"two",3:"three"})
# print(tpl)

# tpl[6][4]="four"
# print(tpl)

# tpl[6].pop(2)
# print(tpl)
# -------------------------------------------
# Set
# ------------------------------------------
# set in set----Not Possible---TypeError--Unhashable Type
# set1={1,12,13,14,15}
# print(set1)

# list in set----Not Possible---TypeError--Unhashable Type
# set1={1,12,13,14,15,[22,23,24,25]}
# print(set1)

# tuple in set----Possible
# set1={1,12,13,14,15,(22,23,24,25)}
# print(set1)

# set2=set1.index(22)
# print(set2)


# dict in set-----Not Possible---TypeError--Unhashable Type
# set1={1,12,13,14,15,{1:"one",2:"two",3:"three"}}
# print(set1)


# t1 = (1,2,3,341)
import oracledb
print(oracledb.__version__)