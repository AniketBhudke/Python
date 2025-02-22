#series
import pandas as pd
import numpy as np
# dict1=[2,3,4,5,np.nan,6]
# df=pd.Series(dict1,index=[11,22,33,44,5,15],name="numbers")
# print(df)
# print("Name Of Series=",df.name)
# print("Values Of Series=",df.values)
# print("Size Of Series=",df.size)
# print("count Of Series=",df.count())


# lst=[11,22,33,44,55,66,77,88,99]
# df=pd.DataFrame(lst,index=[1,2,3,4,5,6,7,8,9])
# print(df.head(4))
# print(df.tail(2))


# lst=[11,22,33,44,55,66,77,88,99]
# df=pd.DataFrame(lst,index=[1,2,3,4,5,6,7,8,9])
# print(df)
# # print(df["a":"d"])
# print(df[3:7])

# 1.adding the series of values
# a=pd.Series([100,200,300,400])
# b=pd.Series([500,600,700,800])
# c=a.add(b)
# print(c)

# a=pd.Series([100,200,300,400],index=[1,2,3,4])
# b=pd.Series([500,600,700,800],index=[1,2,3,4])
# c=a.add(b)
# print(c)

# a=pd.Series([100,200,300,400],index=[1,2,3,33])
# b=pd.Series([500,600,700,800],index=[1,2,3,4])
# c=a.add(b,fill_value=0)
# print(c)

# 2.Subtracting the series of values
# a=pd.Series([100,200,300,400])
# b=pd.Series([500,600,700,800])
# c=a.subtract(b)
# print(c)

# a=pd.Series([100,200,300,400],index=[1,2,3,4])
# b=pd.Series([500,600,700,800],index=[1,2,3,4])
# c=a.subtract(b)
# print(c)

# a=pd.Series([100,200,300,400],index=[1,2,3,33])
# b=pd.Series([500,600,700,800],index=[1,2,3,4])
# c=a.subtract(b,fill_value=0)
# print(c)

# 3.Drop the series of values
# a=pd.Series([100,200,300,400],index=[1,2,3,4])
# a=a.drop(3,inplace=True)
# print(a)

s = pd.Series([10, 20, 30, 40], index=['a', 'b', 'c', 'd'])

s['e']=999
print(s)

