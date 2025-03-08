import pandas as Pd
import numpy as np
dict = {'First Score':[100, 90, np.nan, 95],
        'Second Score': [30, 45, 56, np.nan],
        'Third Score':[np.nan, 40, 80, 98]}
df = Pd.DataFrame(dict)

# print(df.isnull())
# print(df.isna())
# print(df.notna())
# print(df.notnull())


# Filling missing values using fillna(), replace() 
# print(df.fillna(0))
# print(df.replace(to_replace=np.nan,value=1))

# Fillna to replace all NaN
# print(df.fillna(0))

# Fillna on one column
# df['Second Score']=df['Second Score'].fillna(0)
# print(df)

# Fillna() on multiple columns
# df[['Second Score','Third Score']]=df[['Second Score','Third Score']].fillna(0)
# print(df)

# Fillna() on multiple columns with Different Values
# df=df.fillna(value={'Second Score':'1','Third Score':'11'})
# print(df)

# Dropping missing values using dropna() :
print(df.dropna())