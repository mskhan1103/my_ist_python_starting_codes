class salman:
   def __init__(self,x,y):
      self.num=x
      self.den=y

   def __str__(self):
       
      return "{}/{} ".format(self.num,self.den)
   
   def __add__(self,other):
       new_num = self.num*other.den + other.num*self.den
       new_den = self.den*other.den

       return "{}/{} ,".format(new_num,new_den)

   
obj1=salman(3,4)
obj2=salman(1,2)
print(obj1 + obj2)

