"""Write a program that validates name and age as entered by the user to
determine whether the person can cast a vote or not."""
try:
    name=input("Enter the name:")
    age=int(input("Enter age:"))
    if  not name.isalpha():
       raise TypeError

    if age  <= 18:
        raise ValueError
except TypeError:
    print("ENTER VALID NAME")
try:
    if age <= 18:
        raise ValueError

except ValueError:
    print("AGE SHOULD BE GREATER THAN OR EQUAL TO 18")


