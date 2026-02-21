class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def reversed(head):
    prev = None
    current = head
    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node
    return prev

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

new_head = reversed(head)
current = new_head
while current:  
    print(current.data, end=" <- ")
    current = current.next
print("None")