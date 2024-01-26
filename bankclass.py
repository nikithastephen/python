
class bank:
    def __init__(self,name,acc_no,type_acc,balance):
        self.fname=name
        self.num=acc_no
        self.typeacc=type_acc
        self.bal=balance
    def deposit(self,amount1):

        self.bal=self.bal+amount1
        print("Available balance:",self.bal)
    def withdraw(self,amount2):
        if amount2 >=0:
            self.bal=self.bal-amount2
            print("Available balance:", self.bal)
        else:
            print("INSUFFICIENT BALANCE")
    def display(self):
        print("ACCOUNT NAME",self.fname)
        print("ACCOUNT NUMBER", self.num)
        print("ACCOUNT TYPE", self.typeacc)
        print("ACCOUNT BALANCE",self.bal)
name=input("Enter ACCOUNT HOLDER NAME:")
acc_no=int(input("Enter ACCOUNT NUMBER:"))
type_acc=input("Enter ACCOUNT TYPE (savings/current):")
balance=int(input("Enter  ACCOUNT BALANCE:"))
b1=bank(name,acc_no,type_acc,balance,)
amount1=int(input("ENTER AMOUNT TO DEPOSIT:"))
b1.deposit(amount1)
amount2=int(input("ENTER AMOUNT TO WITHDRAW:"))
b1.withdraw(amount2)
b1.display()






