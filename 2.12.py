"""Add ‘ing’ at the end of a given string. If it already ends with ‘ing’, then add ‘ly’"""
str=input("Enter the string:")
if str[-3:]=="ing":
    new=str+"ly"
else:
    new=str+"ing"
print("New string:",new)

