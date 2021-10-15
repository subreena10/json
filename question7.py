import json
# a={Name Abhishek
#  Designation CEO of navgurukul
#  Gender male
#  Age 29}
with open("text.txt","w") as f:
      json.dump(f,indent=4)