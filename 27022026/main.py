# determine if a string is palindrome
def check_palindrome(x):
    x = str(x)
    org = x
    new = x[::-1]
    if org == new:
        print("True")
    else:
        print("False")

check_palindrome(121)

#Return the alphabet sum for each word in a list.

def alphabet_sum(words):
    res = []
    for word in words:
        total = sum(ord(char.lower()) - 96 for char in word if char.isalpha())
        res.append(total)
    return res

words = ["apple", "dog", "library"]
print(alphabet_sum(words))

# Implement a priority queue using a linked list.
class Node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.next = None

class PriorityQueue:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None
    
    def enqueue(self, data, priority):
        new_node = Node(data, priority)

        if self.is_empty() or priority > self.head.priority:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.priority >= priority:
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def dequeue(self):
        if self.is_empty():
            raise Exception("Priority queue is empty")
        
        removed_data = self.head.data
        self.head = self.head.next
        return removed_data
    
    def peek(self):
        if self.is_empty():
            raise Exception("Priority Queue is empty")
        
        return self.head.data
    
    def display(self):
        current = self.head
        while current:
            print(f"Data: {current.data}, Priority: {current.priority}")
            current = current.next

queue = PriorityQueue()

queue.enqueue("Task A", 2)
queue.enqueue("Task B", 1)
queue.enqueue("Task C", 3)
queue.enqueue("Task D", 4)
queue.enqueue("Task E", 5)

queue.display()

print("Dequeued:", queue.dequeue())