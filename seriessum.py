"""Write a program to sum the series 1/1! + 4/2! + 27/3! + ..... + nth term. [ Hint
Use a function to find the factorial of a number]."""
def fact(n):
    if n==0 or n==1:
        return 1
    else:
        return n * fact(n-1)
n=int(input("Enter the limit:"))
result=0
for i in range(1,n+1):
  term=i**i/fact(i)
  result=result+term
print("SUM:",result)
