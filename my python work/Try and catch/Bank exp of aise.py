class bank:
    def __init__(self,balance):
        self.balance=balance

    def withdraw(self,amount):
        self.amount=amount
        if amount<0:
            raise Exception("amount cannot be negative.")
        if amount>self.balance:
            raise Exception("paissa apka itna nahi hai.")
        
        self.balance=self.balance-self.amount
        print(self.balance)


try:
    obj=bank(4000)
    obj.withdraw(1000)
except Exception as e:
    print(e)