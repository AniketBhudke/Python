# import csv # Step-1
# colnames=["TNO","NAME","SUBJECT"] # Step-2
# records=[{"TNO":1000,"NAME":"ROSSUM","SUBJECT":"PYTHON"},
#          {"TNO":2000,"NAME":"TRAVIS","SUBJECT":"NUMPY"},
#          {"TNO":3000,"NAME":"HUNTER","SUBJECT":"MATPLOTLIB"},
#          {"TNO":4000,"NAME":"DENNIS","SUBJECT":"C"},
#          {"TNO":5000,"NAME":"JGOSLING","SUBJECT":"JAVA"} ] # Step-3
# with open("teacher.csv","a") as fp: # Step-4
#      csvdwr=csv.DictWriter(fp,fieldnames=colnames) # Step-5
#      csvdwr.writeheader() # Step-6
#      csvdwr.writerows(records) # Step-7
#      print("CSV File Created with Dict Data---verify")

import csv
colnames=int(input("Enter How many Columns You Want:"))
if colnames<=0:
    print("Invalid Number:")
else:
     col=[]
     for i in range(colnames):
        col_names=input("Enter A Column Name:")
        col.append(col_names)
     else:   
          outer_list=[]
          student_records=int(input("How Many Numbers Of Student records you want tyo insert:"))
          for j in range(student_records):
               dict1={}
               for i in range(len(col)):
                    val=input(f"Enter A Student Number {col[i]}:")
                    dict1[col[i]]=val
               else:     
                    outer_list.append(dict1)
                    print(outer_list)
          else:
               with open("aniket1235.csv","a")as fp:
                    wr=csv.DictWriter(fp,fieldnames=col)
                    wr.writeheader()
                    wr.writerows(outer_list)
                    print("Your CSV File Writed Successfully--Verify")  


                
       


