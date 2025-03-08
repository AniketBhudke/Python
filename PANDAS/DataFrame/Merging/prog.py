import numpy as np
import pandas as pd
data1= [('Jack', 34, 'Sydney', 5) ,
        ('Riti', 31, 'Delhi' , 7) ,
        ('Aadi', 46, 'New York', 11)]
df1 = pd.DataFrame(data1, columns=['Name', 'Age', 'City', 'Score'])

data2= [('Mohit', 34, 'Tokyo', 11) ,
        ('Veena', 31, 'London' , 10) ,
        ('Shaun', 36, 'Las Vegas', 12)]
data3= [('Mark', 47, 'Mumbai',   13) ,
        ('Jose', 43, 'Yokohama', 14) ,
        ('Ramu', 49, 'Paris',    15)]
df2 = pd.DataFrame(data2, columns=['Name', 'Age', 'City', 'Score'])
df3 = pd.DataFrame(data3, columns=['Name', 'Age', 'City', 'Score'])

# df=pd.concat([df1,df2,df3])
# print(df)

#axes=1 column
df=pd.concat([df1,df2,df3],axis=1)
print(df)