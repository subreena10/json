import json
a={"name": "David",
    "class":"I",
    "age": 6  
  }
f=open("question.json","w")
y=json.dump(a,f,indent=4)
print(y)