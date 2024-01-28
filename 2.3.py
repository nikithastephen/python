"""Store a list of first names. Count the occurrences of ‘a’ within the list."""
li=[]
count=0
n=int(input("Enter the number of items:"))
print("enter the items:")
for i in range(0,n):
    j=input()
    li.append(j)
for i in li:
    if i.count('a'):
        count=count+1
print( "NO OF OUCCURENCE:",count)

