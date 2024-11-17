import csv
with open("D:\PYTHON BACKEND\CSV\employee.csv","r") as fp:
    csvdr=csv.DictReader(fp) # here csvdr is an object of <class 'csv.DictReader'>
    recno=1
    for recdict in csvdr:
        print("\tRecord:{}".format(recno))
        for k,v in recdict.items():
            print("\t\t{}--->{}".format(k,v))
        print("-------------------------------------")
        recno=recno+1


