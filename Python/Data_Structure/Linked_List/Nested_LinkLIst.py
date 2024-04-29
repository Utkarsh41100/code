class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class LinkedList:
    def __init__(self):
        self.head=None
    def append(self,data):
        Newnode=Node(data)
        if self.head==None:
            self.head=Newnode
        else:
            current=self.head
            while current.next is not None:
                current=current.next
            current.next=Newnode
            
    def append_LinkedList(self,Linked_List):
        current=Linked_List.head
        while current is not None:
            self.append(current.data)
            current=current.next            

    def display(self):
        current=self.head
        while current is not None:
            print(current.data)
            current=current.next
child2=LinkedList()
Test=LinkedList()
child1=LinkedList()
child2.append(1) 
child2.append(2) 
child2.append(3)
child1.append(6)
child1.append(4)
child1.append(5)
#Test.append_LinkedList(child2)
Test.append_LinkedList(child1)
child1.display()
#child2.display()



#Test.display()


