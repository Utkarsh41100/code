class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
    def display(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next
    def reverse(self):
        current=self.head
        next=None
        previous=None
        while current is not None:
            next=current.next
            current.next=previous
            previous=current
            current=next
        self.head=previous
first = LinkedList()
first.insert_at_end(1)
first.insert_at_end(2)
first.insert_at_end(3)
first.insert_at_end(4)  
first.reverse()  
first.display()   
                 