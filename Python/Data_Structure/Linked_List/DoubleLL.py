class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.prev=None
class Linklist:
    def __init__(self):
        self.head=None
    def insertatlast(self,data):
        Newnode=Node(data)
        if self.head is None:
            self.head=Newnode
            Newnode.next=None
            Newnode.prev=None
        else:
            current=self.head
        while current.next is not None:
            current=current.next
        Newnode.prev=current
        current.next=Newnode
    def insertatbeg(self,data) :
        Newnode=Node(data) 
        if self.head is None :   
            self.head=Newnode
            Newnode.next=None
        else:
            Newnode.next=self.head
            self.head=Newnode
            Newnode.prev=None
    def insertatindex(self,index,data):
        Newnode=Node(data)
        if index==0:
            Newnode.next=self.head
            self.head=Newnode
        else:
            current=self.head
            count=0
            prev=None
            while current.next is not None and count<index:
                prev=current
                current=current.next
                count+=1
            if current.next is None:
                print("Index out of Range")
                return
            else:
                Newnode.prev=prev.next
                Newnode.next=current.next
                current.prev=Newnode
                prev.next=Newnode
    def display(self):
        current=self.head
        while current is not None:
            print(current.data)
            current=current.next

                       
test=Linklist()
test.insertatbeg(3)
test.insertatbeg(3)
test.insertatbeg(3)
test.insertatbeg(3)
test.insertatbeg(3)
test.insertatindex(2,66)
test.insertatlast(888)
test.display()