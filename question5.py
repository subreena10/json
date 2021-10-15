# import json
# x=open("my_file1.json","r")
# y=json.dumps(x)
# print(x)

import json
x='{1+5j:"4.5",7+6j:"6.5",9+2j:"saab"}'
y=json.loads(x)
for i in y.keys():
    if type(i)== complex:
        print(i)
