import json
x={
 "a":  1,
 "a":  2,
 "a":  3, 
 "a": 4,   
 "b": 1, 
 "b": 2
  }
y={}
with open("file6.json","w") as f:
    json.dump(x,f,indent=4)
f.close()
for i in f:
    if i not in y:
        print(i)
