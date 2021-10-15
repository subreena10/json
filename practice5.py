import json
d={1+5j:"4.5",7+6j:"6.5",9+2j:"saab"}
with open("my_file1.json","w") as f:
    json.dump(d,f,indent=4)