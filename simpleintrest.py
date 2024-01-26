#rate of interest
def senior(p,t):
    return (p*12*t)
def others(p,t):
    return(p*10*t)
p=int(input("enter the principle amount:"))
t=int(input("Enter the number of years:"))
a=int(input("Enter the age:"))
if a>=60:
    print("SIMPLE INTEREST",senior(p,t))
else:
    print("SIMPLE INTEREST",senior(p,t))


