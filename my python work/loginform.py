#... login program and indentation
#... email -> abc
#... password -> 1234

email=input("enter your email ............")
password=input("input your passwiord ..............")
 
if email=="abc" and password=="123":
    print("wlcm")
elif email=="abc" and password!="123":
    print("wrong password ")
    while password!="123":
     password=input("enter password again")
elif email!="abc" and password=="123":
    print("wrong email .....")
    while email!="abc":
     input("enter email again .")
else:
    i=1
    while i<3:
     print("Both password and email are incorect ")
     password=int(input("enter again...."))
     email=input("enter email again .....")
     i +=1

    print("tum sa na ho paya ga.")