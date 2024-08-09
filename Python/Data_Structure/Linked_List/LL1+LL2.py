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
    def merge(self,second):
        Merged_List=LinkedList()
        current_first=self.head
        current_second=second.head

        while current_first is not None and current_second is not None:
            if current_first.data>=current_second.data:
                Merged_List.insert_at_end(current_second.data)
                current_second=current_second.next
            else:
                Merged_List.insert_at_end(current_first.data)
                current_first=current_first.next 
        while current_first is not None:
            Merged_List.insert_at_end(current_first.data) 
            current_first=current_first.next
        while current_second is not None:
            Merged_List.insert_at_end(current_second.data)
            current_second=current_second.next
        return Merged_List        

first = LinkedList()
second= LinkedList()
first.insert_at_end(12)
first.insert_at_end(12)
first.insert_at_end(14)
first.insert_at_end(14) 
second.insert_at_end(11)
second.insert_at_end(12)
second.insert_at_end(13) 
second.insert_at_end(14)  
# first.display()   
# second.display()
merged_list=first.merge(second)
merged_list.display()

                 