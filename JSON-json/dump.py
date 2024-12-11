# import json
# dictobj={"EMPNo":100,"NAME":"Travis","sal":5.6,"author":"scientist"}
# with open("emp.json",'a')as fp:
#     json.dump(dictobj,fp)
#     print("Dict Object Data Saved In JSON File---Verify")

#write the data
import json
import sys
class Student:
    def writeData(self):
        while(True):
                dict1={}
                for i in range(5):
                    column=input("Enter a column name:")
                    value=input("Enter the data in column:")
                    dict1[column]=value
                else:
                    filename=input("Enter the File Name That having Extension .json:")
                    with open(filename,'w')as fp:
                        json.dump(dict1,fp)
                        print("Data Inserted in JSON File---Successfully")
                    ch=input("Do you Want To Insert Data In JSon File--Verify")
                    if ch.lower()=="no":
                        sys.exit()

s = Student()
s.writeData()
        