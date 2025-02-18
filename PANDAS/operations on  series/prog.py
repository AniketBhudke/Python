#opeartions

#addition
# import pandas as pd
# a=pd.Series([100,200,300,400,500],index=["a","b","c","d","e"])
# b=pd.Series([10,20,30,40,50],index=["a","b","f","c","e"])
# c=a.add(b)
# print(c)

# import pandas as pd
# a=pd.Series([100,200,300,400,500],index=["a","b","c","d","e"])
# b=pd.Series([10,20,30,40,50],index=["a","b","f","c","e"])
# c=a.add(b,fill_value=0)
# print(c)

#substract
# import pandas as pd
# a=pd.Series([100,200,300,400,500],index=["a","b","c","d","e"])
# b=pd.Series([10,20,30,40,50],index=["a","b","f","c","e"])
# c=a.subtract(b)
# print(c)


# import pandas as pd
# a=pd.Series([100,200,300,400,500],index=["a","b","c","d","e"])
# b=pd.Series([10,20,30,40,50],index=["a","b","f","c","e"])
# c=a.subtract(b,fill_value=0)
# print(c)


#dropping
# import pandas as pd
# a=pd.Series([100,200,300,400,500],index=["a","b","c","d","e"])
# a.drop('a',inplace=True)
# print(a)

import pandas as pd
a=pd.Series(["a","rrr","fff","rrr","fff","rrr","fff","rrr","t"],index=["a","b","c","d","e",'f','g','h','i'])
# a.sort_values(inplace=True,ascending=False)
# print(a)

# maxv=a.nlargest(1)
# print(maxv)

# minv=a.nsmallest(1)
# print(minv)

a=a.describe()
print(a)