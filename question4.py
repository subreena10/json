import json
d= {
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4
    }
with open("myfile.json","w") as f:
    json.dump(d,f,indent=4,sort_keys=True)