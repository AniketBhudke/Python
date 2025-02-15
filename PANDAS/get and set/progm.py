# import pandas as pd
# names = pd.Series(  ['Mark', 'Rita', 'Vicki', 'Justin', 'John', 'Michal'],
#                     index = [11,22,33,44,55,66])
# # print(names[1])

# print(names[11])

# print(names[1:4])
# print("---------------------------")
# print(names[[11,33,44]])


import pandas as pd
a=pd.Series([100,200,300],index=["a","b","c"])
b=pd.Series([10,20,30],index=["x","y","z"])
c=a.add(b,fill_value=0)
print(c)