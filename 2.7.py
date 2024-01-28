"""Create a single string separated with space from two strings by swapping the character
at position 1.
Eg : str1 = “Hello” str2 =”World” , then create a string str3 = “Hollo Werld” [Hint: use
slicing and concatenation ]"""
s1=input("Enter the string 1:")
s2=input("Enter the string 2:")
s3=s1[0]+s2[1]+s1[2:]+" "+s2[0]+s1[1]+s2[2:]
print(s3)
