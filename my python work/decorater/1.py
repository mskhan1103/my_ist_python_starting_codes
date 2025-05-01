# Simple decorator which will add **** line before and after a sentence.

def decoretor(func):
    def wraper():
        print("******************************")
        func()
        print("******************************")
    return wraper

def hello():
    print("Hello everyone.")

a=decoretor(hello)   # wrapper function will be returned here.
a() # and this will basically called a wrapper function to be executed.
