"""Write a program that prompts the user to enter a number. If the number
is positive or zero print it, otherwise raise a ‘ValueError’ Exception."""
num=int(input("Enter an number:"))
try:
    if num<0:
        raise ValueError
    else:
        print(num)
except ValueError:
    print("invalid integer")s