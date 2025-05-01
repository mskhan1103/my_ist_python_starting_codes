class student:
    def __init__(self):
        print("Hello i am in student constructor...........")

    def buy(self):
        print("This is  parent buy()  function.........")

class salman(student):
    def __init__(self):
        print("Hello i am in child constructor .")
        super().__init__()
        print("Hello i am in child constructor again .")
    def buy(self):
        print("Hello i am in child buy() function")
        super().buy()
s1=salman()
s1.buy()