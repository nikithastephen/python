class polygon:
    def getdata(self):
        raise NotImplementedError
    def area(self):
        raise NotImplementedError
class rectangle(polygon):
    def getdata(self):
       print("RECTANGLE")
       self.l=int(input("Enter the length:"))
       self.b=int(input("Enter the breath:"))
    def area(self):
        print("AREA:",self.l*self.b)
class traingle(polygon):
    def getdata(self):
        print("TRIANGLE")
        self.h=int(input("Enter the height:"))
        self.b=int(input("Enter the base:"))
    def area(self):
        print("AREA:",0.5*self.b*self.h)
r=rectangle()
r.getdata()
r.area()
t=traingle()
t.getdata()
t.area()






