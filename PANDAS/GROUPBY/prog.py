import pandas as pd
import numpy as np
#create DataFrame
df = pd.DataFrame({'team': ['A', 'A', 'A', 'A', 'B', 'B', 'B', 'B'],
                   'points': [30, 22, 19, 14, 14, 11, 20, 28]})

#view DataFrame
print(df)
print("-------------------------------")

tgd=df.groupby("team")
for grpname,grpdata in tgd:
    print(grpname,grpdata)