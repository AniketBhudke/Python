import csv
with open("d.docs.live.net//bbdd99eb4f593d05//Documents//cyber_impact_activity(9).csv","r") as fp:
    csvdr=csv.DictReader(fp) # here csvdr is an object of <class 'csv.DictReader'>
    for recdict in csvdr:
        for k,v in recdict.items():
            print("\t\t{}--->{}".format(k,v))
        print("-------------------------------------")
        
# class student:
#     @staticmethod
#     def csvReader():gamer
#         while(True):
#                     filename=input("Enter The File Name:")
#                     with open(filename,'r')as fp:
#                         filepointer=csv.DictReader(fp)
#                         for records in filepointer:
#                             for key,value in records.items():
#                                 print(f"{key}--->{value}")
#                             print()
#                         print("You  Record Getting Successfully--Verify")        
#                     ch=input("Do you Want To Read Any Other File Data:(yes/no)")
#                     if ch.lower()=="no":
#                         break 
# s1 = student()
# s1.csvReader()


#user=input()
#lst=[user,user]
#guess number by user index

# class linearSearch:
#     def linearSearchExample(self):
#         lst=[]
#         size=int(input("How Many Elment You want in the List:"))
#         for i in range(size):
#             value=int(input("Enter A Number:"))
#             lst.append(value)
#         else:
#             search_ele=int(input("Enter A Number That You want to Search in List:"))
#             for i in range(len(lst)):
#                 return i if lst[i]==search_ele else -1
        
# l1 = linearSearch()
# res=l1.linearSearchExample()                 
# print(res)