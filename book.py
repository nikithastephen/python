"""Create a class Publisher with attributes publisher id and publisher
name. Derive class Book from Publisher with attributes title and author.
Derive class Python from Book with attributes price and no_of_pages.
Write a program that displays information about a Python book. Use
base class constructor invocation """
class publisher:
    def getpublisher(self,publisher_id,name):
        self.publisher_id=publisher_id
        self.name=name
class book(publisher):
    def getbook(self,title,author):
        self.title=title
        self.author=author
class python(book):
    def getdet(self,price,no):
        self.price=price
        self.no=no
class information(python):
    def putdata(self):
        print("PUBLISHER ID:",self.publisher_id)
        print("PUBLISHER NAME:",self.name)
        print("BOOK TITLE:",self.title)
        print("BOOK AUTHOR:",self.author)
        print("PRICE:",self.price)
        print("NO OF PAGES:",self.no)
i=information()
publisher_id=int(input("Enter publisher id:"))
name=input("Enter name:")
title=input("Enter title:")
author=input("Enter author:")
price=int(input("Enter price:"))
no=int(input("Enter no of pages:"))
i.getpublisher(publisher_id,name)
i.getbook(title,author)
i.getdet(price,no)
i.putdata()