# import csv
# row=["name","Class","marks","Attendance"]
# rows=[["kunal","Bca",99,90],
#       ["aniket","bca",78,89],
#       ["harsha","bca",89,98]]
# with open ("aniket1245.csv",'a')as fp:
#     csvwr=csv.writer(fp)
#     csvwr.writerow(row)
#     csvwr.writerows(rows)

# with open("aniket1245.csv",'r') as fp:
#     csvwr=csv.reader(fp)
#     for fields in csvwr:
#         for data in fields:
#             print("\t{}".format(data),end="\t")
#         print()    


import csv
import sys
class Writer:
    def WriterOpearation(self):
        while(True):
            try:
                column_size=int(input("Enter How Many Column You Want:"))
                column=[]
                if column_size<=0:
                    print(f"{column_size}it is inavalid input")
                else:
                    for i in range(column_size):
                        column_name=input("Enter The Column Name:")
                        column.append(column_name)
                    else:
                        outer_column_data=[]
                        record_size=int(input("How many Number of Student Record you want to Enter:"))
                        for i in range(record_size):
                            inner_column_data=[]
                            for j in range(len(column)):    
                                sno=input(f"Enter the {column[j]}:")#mla eth dynamysism pahije
                                if j==0 or j==2:
                                    sno = int(sno)
                                inner_column_data.append(sno)
                            outer_column_data.append(inner_column_data)
                        else:
                            filename=input("Enter The File Name With .csv Extension:")
                            with open(filename,'a',newline='')as fp:
                                csvwr=csv.writer(fp)                                
                                csvwr.writerow(column)
                                csvwr.writerows(outer_column_data)
                            print(" Record inserted in the file Sucessfully--Verify")                                             
                        ch=input("Do You want To Enter Data(yes/no):")
                        if ch.lower()=="no":
                            print("thnx for using These Program:")
                            sys.exit()
            except ValueError:
                print("Don't Enter Alnums,strs and symbols: ")

w = Writer()
w.WriterOpearation()
        