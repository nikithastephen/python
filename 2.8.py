"""10. Write a python program to read two lists color-list1 and color-list2. Print out all colors
from color-list1 not contained in color-list2."""
l1=[]
l2=[]
m=int(input("Enter the number of items in l1:"))
for i in range(0,m):
    j=input()
    l1.append(j)
n=int(input("Enter the number of items in l2:"))
for i in range(0,n):
    j=input()
    l2.append(j)
l3=[]
for i in l1:
    if i not in l2:
        l3.append(i)
print("Colors only in l1:",l3)
