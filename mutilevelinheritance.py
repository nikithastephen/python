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
class total(marks):
     def totalmark(self):
         print("TOTAL MARKS:",self.mark1+self.mark2)

name=input("Enter your name:")
rollno=int(input("Enter your rollno:"))
age=int(input("Enter your age:"))
mark1=float(input("Enter your mark1:"))
mark2=float(input("Enter yoour mark2:"))
obj=total()
obj.setdata(name,rollno,age)
obj.putdata()
obj.setmarks(mark1,mark2)
obj.putmarks()
obj.totalmark()