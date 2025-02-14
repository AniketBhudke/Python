# import csv
# with open("aniket.csv","r") as fp:
#     csvr=csv.reader(fp) # Here csvr is an object of <class, _csv.reader>
#     for record in csvr: # here record is an object of <class, list>
#         for val in record:
#             print("\t{}".format(val),end="\t")
#         print()

# d={"EmpNo":100,"Name":"Travis","Sal":5.6,"Author":"Scientist"}
# print("Dict Data={}   Type={}".format(d,type(d)))
# print("-"*70)
# #Covert Dict Object data to JSON Str Data format
# jsonstrdata=str(d)
# print("Json Str Data={}  Type={}".format(jsonstrdata,type(jsonstrdata)))
# print("-"*70)

import json
try:
	with open("data.json","r") as fp:
			dictobj=json.load(fp)
			print("Dict Object Data={}".format(dictobj))
			print("--------------------------------------------------------------------")
			for k ,v in dictobj.items():
				print("{}".format(k))
				for key,val in v.items():
					print("\t{}---->{}".format(key,val))
			print("--------------------------------------------------------------------")
except FileNotFoundError:
	print("File does not Exist")