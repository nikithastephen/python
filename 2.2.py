"""Write a program to prompt the user for a list of integers. For all values greater than 100,
store ‘over’ instead."""
li=[]
n=int(input("Enter the number of items:"))
print("enter the items:")
for i in range(0,n)
    j=int(input())
    if j > 100:
        li.append("over")
    else:
        li.append(j)
print(li)
