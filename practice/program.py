# #file
# # with open("ae12.data","a")as fp:
# #     dict1={}
# #     SNo=int(input("Enter A numbr:"))
# #     SName=input("Enter A Name:")
# #     SMarks=int(input("Enter a marks of student"))
# #     dict1["SNo"]=SNo
# #     dict1["SName"]=SName
# #     dict1["SMarks"]=SMarks
# #     fp.writelines(str(dict1))
# #     print("Data Write in the File--Successfully")
# # try:
# #     with open("anike.data",'r+')as fp:
# #         lst1=["aniket","vijay","Bhudke","a","aa"] 
# #         fp.writelines(lst1)
# #         print("File Created Successfully")
# #         user=input("Do you want to Read the Data--Yes/No:")
# #         if user=="Yes":
# #             fp.seek(0)
# #             rw=fp.read()
# #             print(rw)
# #         else:
# #             print("Thank you...!")    
# # except  FileExistsError:
# #     print("File Already Exists--Try Again")   
    

# #csv file

# #witer ----writerow()--writerowws()
# # import csv
# # row=["Name","no","Marks"]
# # rows=[["Aniket",1,89],
# #       ["harsh",2,88],
# #       ["kunal",3,78],
# #       ["sagr",4,67]]
# # with open("a1.csv","a")as fp:
# #     csvwr=csv.writer(fp)
# #     csvwr.writerow(row)
# #     csvwr.writerows(rows)
# #     print("File Created Successfully")

# # row=["rno","name","Class","marks"]
# # rows=[{"rno":1,"Name":"aniket","Class":"Bca","marks":99},
# #       {"rno":2,"Name":"Harshal","Class":"Bsc","Marks":90},
# #       {"rno":3,"Name":"Kunaal","Class":"bca","Marks":99}]
# # with open("lkunal.csv")


# l1=[1,2,10,10,10,10,5,10,10,10,3,4]
# # l2=[]
# # for value in l1:
# #     if value == 10:
# #         continue
# #     else:
# #         l2.append(value)
# # print(l2)        

# l1=[1,2,10,10,10,10,5,10,10,10,3,4]
# # length=len(l1)
# # for i in range(0,length-1):
# #     if l1[i]==10:
# #         l1.remove(l1[i])
# # print(l1)        

# function a(res):
    


# res=list(filter(a))
# print(res)



# dict1={len(word):word for word in input().split()}
# print(dict1[max(dict1.keys())])












# # l1=[1,2,10,10,10,10,5,10,10,10,3,4,4]
# # dict1={val:l1.count(val) for val in l1}
# # print(dict1)