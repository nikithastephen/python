"""Create a Rectangle class with attributes length and breadth and
methods to find area and perimeter. Compare two Rectangle objects by
their area."""
class rectangle:
    def setdata(self):
        self.l=int(input("enter the length:"))
        self.b=int(input("enter the breadth:"))


    def perimerter(self):
       return(self.l+self.b)
    def area(self):
        return(self.l*self.b)


r1=rectangle()
r1.setdata()
print("PERIMETER1:",r1.perimerter())
area1=r1.area()
print("area1:",area1)
r2=rectangle()
r2.setdata()
print("PERIMETER2:",r2.perimerter())
area2=r2.area()
print("area2:",area2)
if area1 > area2:
    print("The first object has larger area")
else:
    print("The second object has larger area")