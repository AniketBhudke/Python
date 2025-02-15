# import pandas as pd

# #int
# a=12
# b=pd.Series(a)
# print(b)

# #float

# a=12.7
# b=pd.Series(a)
# print(b)

# #complex

# a=12 + 3j
# b=pd.Series(a)
# print(b)

# # #boolean
# a=True
# b=pd.Series(a)
# print(b)

# #str
# a="aniket"
# b=pd.Series(a)
# print(b)

# # range
# r=range(10,21,1)
# a=pd.Series(r)
# print(a)

# # #list
# a=[11,22,33,44,55]
# b=pd.Series(a)
# print(b)

# lst=["aniket",22,22.4,2+5j]
# df=pd.Series(lst,index=[11,22,33,44],name="table")
# print(df)

# print(df[11])

# print(df.name)
# print(df.values)
# print(df.size)
# print(df.empty)
# s=df.head(3)
# print(s)

# s=df.tail(3)
# print(s)

# print(df.count)

# import  pandas as pd
# users = pd.Series(  ['Mark', 'Rita', 'Vicki', 'Justin', 'John', 'Michal'],
#                     index = ['a', 'b', 'c', 'd', 'e', 'f'],
#                     name = "Students")
# # print(users)
# print(users.values)


#add
import pandas as pd
a=pd.Series([100,200,300,400,500],index=["a","b","h","d","e"])
b=pd.Series([10,20,30,40,50],index=["a","b","f","c","e"])
print("----------------------------------")
c=a.add(b)
print(c)
print("----------------------------------")
c=a.add(b,fill_value=0)
print(c)


c=a.sub(b)
print(c)
print("----------------------------------")
c=a.sub(b,fill_value=0)
print(c)
