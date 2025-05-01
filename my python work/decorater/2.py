def decoretor(func):
    def wraper():
        print("******************************")
        func()
        print("******************************")
    return wraper
@decoretor
def hello():
    print("Hello everyone.")
@decoretor
def hello1():
    print("Hello1 everyone.")
hello()
hello1()



