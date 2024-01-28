"""Accept a list of words and return the length of the longest word."""
li=[]
lar=0
n=int(input("Enter the number of words:"))
for i in range(0,n):
    j=input()
    li.append(j)
for i in li:
    if len(i)>lar:
        lar=len(i)
print("The largest word:",lar)
