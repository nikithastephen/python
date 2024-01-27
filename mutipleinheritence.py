class student:
    def setdata(self,name,rollno,age):
        self.name=name
        self.rollno=rollno
        self.age=age
    def putdata(self):
        print("NAME:",self.name)
        print("ROLL NO:",self.rollno)
        print("AGE:",self.age)
class marks(student):
    def setmarks(self,mark1, mark2):
        self.mark1=mark1
        self.mark2=mark2
    def putmarks(self):
        print("MARK1:",self.mark1)
        print("MARK2:",self.mark2)
        print("TOTAL MARKS:",self.mark1+self.mark2)
class sports:
    def setsport(self,smark):
        self.smark=smark
    def putsport(self):
        print("SPORT MARK:",self.smark)
class total(marks,sports):
    def details(self):
        print("OVERALL MARKS:",self.mark1+self.mark2+self.smark)
name=input("Enter your name:")
rollno=int(input("Enter your rollno:"))
age=int(input("Enter your age:"))
mark1=float(input("Enter your mark1:"))
mark2=float(input("Enter your mark2:"))
smark=float(input("Eneter your sports marks:"))
obj=total()
obj.setdata(name,rollno,age)
obj.putdata()
obj.setmarks(mark1,mark2)
obj.putmarks()
obj.setsport(smark)
obj.putsport()
obj.details()
SAZ