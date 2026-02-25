# create an inventory system

class Inventory():
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        self.books[book] = 1

Amazon = Inventory()
Amazon.add_book("Programming Python")
print(Amazon.books)