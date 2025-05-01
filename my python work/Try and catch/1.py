try:
    f=open("Hello.txt","r")
    print(f.read())
    a=input("Enter any no")
    print(a+" ")
    m=4
    print(m)
except FileNotFoundError:
    print("file not found.")
except TypeError:
    print("type error.")
except Exception as e:
    print(e)
finally:
    print("Finally is executed all the time.")


    