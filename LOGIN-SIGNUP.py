import json
import re
import os.path
user=input("Do you want to signup or login: ")
file_exists=os.path.exists("love.json")
def dump(obj):
    with open("love.json","w") as f:
        json.dump(obj,f,indent=2)
if user=="signup":
    username=input("Enter ur userame: ")
    print("Create a strong password Use specail characters.")
    password1=input("Enter ur password: ")
    if re.search ("[a-z A-Z]",password1) and re.search ("[@%$#!]",password1) and re.search ("[0-9]",password1) :
        password2=input("Enter your password agian: ")
        if password1==password2:
            print("Matching")
            date_of_birth=input("enter your date of birth: ")
            gender=input("entere your gender\n1.)F\n2.)M\n3.)others: ")
            hobbies=("enter your hobbies: ")
            description=input("Enter your bio: ")
            dic={"username":username,"password":password1,"re_password":password2,"date_of_birth":date_of_birth,
                "gender":gender,"hobby":hobbies,"description":description}
            if file_exists==True:
                with open("love.json","w") as file:
                    d=file.write()
                    p=json.loads(d)
                    p.append(dic)
                    dump(p)
            else:
                with open ("love.json","w") as file:
                    json.dump([dic],file,indent=4)
        else:
            print("Not matching")
    else:
        print("use special character and one number,character")
else:
    if user=="login":
        username=input("enter your nusername: ")
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
    
