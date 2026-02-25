# create an inventory system

class Inventory():
    def __init__(self):
        self.books = {}

    def add_book(self, book):
        self.books[book] = 1

Amazon = Inventory()
Amazon.add_book("Programming Python")
print(Amazon.books)

# create a linked list
class Node():
    def __init__(self, data):
        self.data = data
        self.next = None

def traverse(head):
    currentNode = head
    while currentNode:
        print(currentNode.data, end=" -> ")
        currentNode = currentNode.next
    print("null")

node1 = Node(8)
node2 = Node(12)
node3 = Node(2)
node4 = Node(5)

node1.next = node2
node2.next = node3
node3.next = node4

traverse(node1)