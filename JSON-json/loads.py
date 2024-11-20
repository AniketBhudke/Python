import json
jsonData='{"Name":"Aniket","Class":"BCA","Marks":78}'
Dictdata=json.loads(jsonData)
print(Dictdata)
for k,v in Dictdata.items():
    print(f"\t{k}:{v}\t")
