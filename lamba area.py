"""Write lambda functions to find the area of square, rectangle and triangle."""
s=int(input("Enter the side of the square:"))
l=int(input("Enter the length of the rectange:"))
w=int(input("Enter the width of the rectangle:"))
b=int(input("Enter the base of the triangle:"))
h=int(input("Enter the height of the triangle:"))
square=lambda s:4*s
print("Area of the square:",square(s))
rectangle=lambda l,w:l*w
print("Area of the rectangle:",rectangle(l,w))
triangle=lambda b,h:0.5*b*h
print("Area of the triangle:",triangle(b,h))
