"""""
Write OOP classes to handle the following scenarios:
A user can create and view 2D coordinates
A user can find out the distance between 2 coordinates
A user can find find the distance of a coordinate from origin
A user can check if a point lies on a given line
A user can find the distance between a given 2D point and a given line
"""""
class Point:
    def __init__(self,x,y):
        self.x_cod=x
        self.y_cod=y

    def __str__(self):
        return "<{},{}>".format(self.x_cod,self.y_cod)
    
    def find_distance(self,other):
        return ((self.x_cod-other.x_cod)**2+(self.y_cod-other.y_cod)**2)**0.5
       # return ((self.x_cod - other.x_cod)**2 + (self.y_cod - other.y_cod)**2)**0.5

    def distance_from_origin(self):
        return (self.x_cod**2+self.y_cod**2)**0.5

class Line:
    def __init__(self,A,B,C):
        self.A=A
        self.B=B
        self.C=C
        
    def __str__(self):
        return "{}x + {}y + {}".format(self.A,self.B,self.C)
    
    def point_on_line(line,point):
     if line.A*point.x_cod + line.B*point.y_cod + line.C == 0:
       return "lies on the line"
     else:
       return "does not lie on the line"
     
    def distance_bt_given_pts(line,point):
       return  abs(line.A*point.x_cod + line.B*point.y_cod + line.C)/(line.A**2 + line.B**2)**0.5



    

p1=Point(2,1)
#p2=Point(13,12)
#x=p1.find_distance(p2)
#print(x)
x2=p1.distance_from_origin()
print(x2)
l1=Line(1,2,-6)
print(l1)
l2=l1.point_on_line(p1)
print(l2)
l3=l1.distance_bt_given_pts(p1)
print(l3)