"""Write a program to prompt the user to enter two lists of integers and check
(a) Whether lists are of the same length.
(b) Whether the list sums to the same value.
(c) Whether any value occurs in both Lists."""
l1=[]
l2=[]
n=int(input("Enter the number of items of list1:"))
print("enter the items of list1:")
for i in range(0,n):
    j=int(input())
    l1.append(j)
m=int(input("Enter the number of items of list2:"))
print("enter the items of list:")
for i in range(0,m):
    j= int(input())
    l2.append(j)
if len(l1) == len(l2):
    print(l1,"and",l2,"are equal")
else:
    print(l1, "and", l2, "are  not equal")
sum1=0
sum2=0
for i in l1:
    sum1=sum1+i
for j in l2:
    sum2=sum2+j
if sum1==sum2:
    print("SUM are EQUAL")
else:
    print("SUM are NOT EQUAL")
for i in l1:
    if i in l2:
        print(i,"is in both the list")


