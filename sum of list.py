li=[]
sum=0
n=int(input("Enter the number of items:"))
for i in range(0,n):
    j=int(input())
    li.append(j)
for i in li:
    sum=sum+i
print("SUM:",sum)