#Program for Reading JSON File Data into Dict Object 
import json
class Student:
    def readData(self):
        with open("emp.json",'r')as fp:
            readdata=json.load(fp)
            for key , value in readdata.items():
                print(f"{key}--->{value}")

s = Student()
s.readData()
