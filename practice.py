import json
d = {"Name":"Ram", 
     "Class":"IV", 
     "Age":9 }
with open("file.json","w") as x:
    json.dump(d,x,indent=4)

