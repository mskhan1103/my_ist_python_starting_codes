# Example of AGGREgation :
class Customer:
    def __init__(self,name,gender,address):
        self.name=name
        self.gender=gender
        self.address=address
    def print_address(self):
        print(self.address.get_city(),self.address.pin,self.address.state)

    def edit_profile(self,new_name,new_city,new_pin,new_state):
        self.name = new_name
        self.address.edit_address(new_city,new_pin,new_state)




class Address:
    def __init__(self,city,pin,state):
        self._city=city
        self.pin=pin
        self.state=state
    def get_city(self):
        return self._city
    def edit_address(self,city,pin,state):
        
        self._city=city
     
        self.pin=pin
        self.state=state

add1=Address("LM",1010,"KPK")
cust1=Customer("salamn","male",add1)
cust1.print_address()
        
add2=Address("LM",1010210101,"KPK,wanda zeran")
cust2=Customer("salamn","male",add2)
cust2.print_address()

cust2.edit_profile("khan","abakhel",222,"abc")
cust2.print_address()
    