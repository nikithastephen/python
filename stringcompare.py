"""Write a function called compare which takes two strings S1 and S2 and an
integer n as arguments. The function should return True if the first n
characters of both the strings are the same else the function should return
False."""
def compare(s1,s2,n):
    if s1[:n]==s2[:n]:
        print("TRUE,The first",n,"characters are EQUAL")
    else:
        print("FALSE,The first",n,"characters are NOT EQUAL")

s1=input("Enter the STRING1:")
s2=input("Enter the STRING2:")
n=int(input("Enter the number of first characters to be checked:"))
compare(s1,s2,n)