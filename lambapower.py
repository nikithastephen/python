
"""Write a program to display powers of 2 using anonymous function.[Hint use
map and lambda function)"""
n=int(input("Enter the limit: "))
power=lambda n:list(map(lambda i:2**i,range(n)))
result=power(n)
print(result)

