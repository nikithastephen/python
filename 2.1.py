"""Create a string from the given string where the first and last character are exchanged."""
str=input("Enter the string:")
new=str[-1]+str[1:-1]+str[0]
print(new)
