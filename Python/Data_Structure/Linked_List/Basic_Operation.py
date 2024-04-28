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

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_index(self, index, data):
        if index < 0:
            print("Index out of range")
            return
        if index == 0:
            self.insert_at_beginning(data)
            return
        current = self.head
        count = 0
        while current is not None:
            if count == index - 1:
                new_node = Node(data)
                new_node.next = current.next
                current.next = new_node
                return
            current = current.next
            count += 1
        print("Index out of range")

    def deleteatbeg(self):
        if self.head is None:
            print("LinkedList is empty")
            return
        else:
            self.head = self.head.next

    def deleteatlast(self):
        if self.head is None:
            print("LinkedList is empty")
            return
        current = self.head
        prev = None
        while current.next is not None:
            prev = current
            current = current.next
        if prev is not None:
            prev.next = None
        else:
            self.head = None

    def deleteatindex(self, index):
        if self.head is None:
            print("LinkedList is empty")
            return
        if index < 0:
            print("Index out of range")
            return
        if index == 0:
            self.head = self.head.next
            return
        current = self.head
        prev = None
        count = 0
        while current is not None and count < index:
            prev = current
            current = current.next
            count += 1
        if current is None:
            print("Index out of range")
            return
        prev.next = current.next

    def display(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next

# Testing the LinkedList

first = LinkedList()
first.insert_at_beginning(100)
first.insert_at_end(10)
first.insert_at_index(2, 987)
first.insert_at_end(130)
first.insert_at_end(1)
first.insert_at_end(95)
first.insert_at_end(20)
first.deleteatbeg()
first.deleteatlast()
first.deleteatindex(2)
first.display()
