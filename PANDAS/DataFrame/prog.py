# # a) By using list / tuple
# import pandas as pd
# # lst=[10,30,50,60,80,90]
# # df=pd.DataFrame(lst)
# # print(df)

# # lst=[["aniket",34,"bca"],["sagar",33,"bsc"],["kunal",16,"bcom"],["sumit",9,"msc"]]
# # df=pd.DataFrame(lst,index=["s1","s2","s3","s4"],columns=['Name','Age','Class'])
# # print(df)

# # b) By using dict

# # dictdata={"Names":["Rossum","Gosling","Ritche","McKinney"],"Subjects":["Python","Java","C","Pandas"],"Ages":[65,80,85,55]  }
# # df=pd.DataFrame(dictdata)
# # print(df)

# # dictdata={"Names":["Rossum","Gosling","Ritche","McKinney"],"Subjects":["Python","Java","C","Pandas"],"Ages":[65,80,85,55]  }
# # df=pd.DataFrame(dictdata,index=["student1","Student2","Student3","student4"])
# # print(df)


# # d) By using Series
# sdata=pd.Series({"IntMarks":[10,20,30,40],"ExtMarks":[80,75,65,50]})
# print(sdata)
# sdata={"IntMarks":[10,20,30,40],"ExtMarks":[80,75,65,50]}
# df=pd.DataFrame(sdata)
# print(df)
# # e) By using ndarray of numpy
# import numpy as np
# nd=np.arange(9).reshape(3,3)
# df=pd.DataFrame(nd)
# print(df)


# # f) By using CSV File (Comma Separated Values)
# import pandas as pd
# df=pd.read_csv("D:\\PYTHON BACKEND\\saniket1.csv")
# print(df)

#attributes of datframes



