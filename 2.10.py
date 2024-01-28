"""a list of integers, create a list after removing even numbers."""
li=[]
n=int(input("Enter the number of items in the list:"))
for i in range(0,n):
    j=int(input())
    if j%2!=0:
        li.append(j)
print(li)
