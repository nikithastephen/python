""" Write a program to print the Fibonacci series using recursion."""
def fib(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)
m=int(input("Enter valid integer:"))
print("FIBONACCI SERIES:")
for i in range(m):
    print(fib(i))




