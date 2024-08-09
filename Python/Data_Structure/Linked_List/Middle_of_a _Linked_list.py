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
    def check(self):
        count=0
        current=self.head
        while current !=None:
            current=current.next
            count+=1
        middle=count//2
        current=self.head
        for a in range(middle):
            current=current.next
        print(f"Middle node data: {current.data}")                    
first = LinkedList()
first.insert_at_end(130)
first.insert_at_end(1)
first.insert_at_end(95)
first.insert_at_end(20)    
first.display()   
first.check()                 