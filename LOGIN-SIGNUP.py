import json
import re
import os.path
user=input("Do you want to signup or login: ")
file_exists=os.path.exists("/home/sabrina/Desktop/json/love.json")
def dump(obj):
    with open("/home/sabrina/Desktop/json/love.json","w") as f:
        json.dump(obj,f,indent=2)
if user=="signup":
    username=input("Enter ur userame: ")
    
    print("Create a strong password Use specail characters.")
    password1=input("Enter ur password: ")
    f= open("love.json","r")
    name=f.read()
    if re.search ("[a-z A-Z]",password1) and re.search ("[@%$#!]",password1) and re.search ("[0-9]",password1) :
        password2=input("Enter your password agian: ")
        if password1==password2:
            print("Matching")
        else:
            print("Not matching")
        list1=["username","password"]
        list2=[username,password2]
        list3=[]
        dic1={}
        i=0
        while i<=1:
            list3.append((list1[i],list2[i]))
            i=i+1
        dic1.update(list3)
        if username in name:
            print(username,"already exists")

        else:
            print(username,"you signed up successfully")
            print("Please enter the following details:")
        
            date_of_birth=input("enter your date of birth: ")
            gender=input("entere your gender\n1.)F\n2.)M\n3.)others: ")
            hobbies=input("enter your hobbies: ")
            description=input("Enter your bio: ")
            dic={"username":username,"password1":password1,"password2":password2,"date_of_birth":date_of_birth,
                "gender":gender,"hobbies":hobbies,"description":description}
            if file_exists==True:
                with open("/home/sabrina/Desktop/json/love.json","r") as file:
                    d=file.read()
                    p=json.loads(d)
                    p.append(dic)
                    dump(p)
            else:
                with open ("love.json","w") as file:
                    json.dump([dic],file,indent=4)
      
            
    else:
        print("use special character and one number,character")

else:
    if user=="login":
        username=input("enter your username: ")
        password=input("enter your password: ")
        with open("love.json","r") as file1:
            a=file1.read()
            b=json.loads(a)
            for i in b:
                if i["username"]==username:
                    if i["password"]==password:
                        print("login successfull")
                    else :
                        print("Wrong password")
    else:
        print("Wrong id")
    