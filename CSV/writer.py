import csv
row=["name","Class","marks","Attendance"]
rows=[["kunal","Bca",99,90],
      ["aniket","bca",78,89],
      ["harsha","bca",89,98]]
with open ("aniket1245.csv",'a')as fp:
    csvwr=csv.writer(fp)
    csvwr.writerow(row)
    csvwr.writerows(rows)

with open("aniket1245.csv",'r') as fp:
    csvwr=csv.reader(fp)
    for fields in csvwr:
        for data in fields:
            print("\t{}".format(data),end="\t")
        print()    
