"""Write a Python program to count the occurrences of each word in a line of text.
Hint: use split() function and dictionary
Sample input : the quick brown fox jumps over the lazy dog"""
str=input("Enter the line of text with spaces btw each word:").split(" ")
dict={}

for i in str:
    if i in dict:
        dict[i]=dict[i]+1
    else:
        dict[i] = 1
for i,j in dict.items():
    print(i,j)

