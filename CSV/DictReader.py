import csv
with open("aniket.csv","r") as fp:
    csvdr=csv.DictReader(fp) # here csvdr is an object of <class 'csv.DictReader'>
    for recdict in csvdr:
        for k,v in recdict.items():
            print("\t\t{}--->{}".format(k,v))
        print("-------------------------------------")
