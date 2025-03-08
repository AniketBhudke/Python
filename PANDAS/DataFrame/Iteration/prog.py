import numpy as np
import pandas as pd
lst=[[10,20,30,40,50],["RS","TR","SS","DR","JH"],[1.2,2.3,4.5,5.6,6.7]]
df=pd.DataFrame(lst)
print(df)
print("-------------------------")
for rec in df.iterrows():
    print("Row Index:",rec[0])
    print("Record Values:",rec[1].values)
print("-------------------------")

for (rind,rvals)in df.iterrows():
    print("Row Index:",rind)
    print("Record Values:",rvals.values)
print("----------------------") 
for i in range(df.shape[0]):
    print("Row Index:",i)
    print("\tRow Values=",df.loc[i].values)
print("-------------------------------")
#3.Iterating the DataFrame Object Data by using  Col Names

lst=[[10,20,30,40,50],["RS","TR","SS","DR","JH"],[1.2,2.3,4.5,5.6,6.7]]
df=pd.DataFrame(lst,columns=["Rec1","Rec2","Rec3","Rec4","Rec5"])
print(df)
print("--------------------------------")

for col in df.columns:
    print("Column Name:",col)
    print("Column Values:",df[col].values)
print("-------------------------")

#4. Iterating the DataFrame Object Data by using Column  Indices
lst=[[10,20,30,40,50],["RS","TR","SS","DR","JH"],[1.2,2.3,4.5,5.6,6.7]]
df=pd.DataFrame(lst)
print(df)
print("------------------------------")

#4. Iterating the DataFrame Object Data by using Column  Indices
for colindex in range(df.shape[1]):
    print("Column Index:{}".format(colindex))
    print("\tColumn Data={}".format(df.iloc[:,colindex].values))
