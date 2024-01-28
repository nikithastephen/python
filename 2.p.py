"""Create a list of colors from comma-separated color names entered by the user. Display
first and last colors."""
str=input("Enter the list of colors seperated by comas:").split(",")
print("FRIST:",str[0])
print("LAST:",str[-1])