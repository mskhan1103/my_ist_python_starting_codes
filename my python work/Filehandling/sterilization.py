import json
l=[1,2,3,4,45]
with open("json.demo","w") as f:
    print(json.dump(l,f,indent=4))


import json
with open("json.demo","r") as f:
    d=json.load(f)
    print(d)