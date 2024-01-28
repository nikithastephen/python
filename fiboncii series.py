"""Write a program to generate Fibonacci series of N terms."""
n=int(input("Enter the limit:"))
a=0
b=1
i=0
print("FIBONACCI SERIES:")
while i<n:
    print(a)
    c=a+b
    a=b
    b=c
    i=i+1


