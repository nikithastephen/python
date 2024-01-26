#function to check odd or even
def check(n):
    if n==0:
        print(n,"is neither odd or even")
    elif n%2==0:
        print(n,"is an even number")
    else:
        print(n,"is an odd number")
n=int(input("Enter a valid integer:"))
check(n)

