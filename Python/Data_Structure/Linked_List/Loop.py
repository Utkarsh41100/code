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
    def create_loop(self,position) :
        if self.head==None:
            return
        count=0
        current=self.head
        loopointer=None
        while current.next is not None:
            if count==position:
                loopointer=current
            count+=1
            current=current.next
        if loopointer:
            current.next=loopointer        
    def checkloop(self):
        current=self.head
        pointer=None
        while current.next is not None:
            pointer=current.next
        
first = LinkedList()
first.insert_at_end(1)
first.insert_at_end(2)
first.insert_at_end(3)
first.insert_at_end(4)  