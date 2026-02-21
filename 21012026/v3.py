class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def display(self):
        current_node = self.head
        while current_node:
            print(current_node, end=" -> ")
            current_node = current_node.next
        print("None")

llist = LinkedList()

llist.append(10)
llist.append(20)
llist.append(30)
llist.append(40)
llist.append(50)
llist.display()

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(16)
node2 = Node(2)
node3 = Node(145)
node4 = Node(88)

node1.next = node2
node2.next = node3
node3.next = node4

head = node1

current = head

while current:
    print(current.data, end=" -> ")
    current = current.next
print("None")