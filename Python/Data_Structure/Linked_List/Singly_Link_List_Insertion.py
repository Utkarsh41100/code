class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class linklist:
    def __init__(self):
        self.head=None
    def Insertnode(self,data):
        newnode=Node(data)
        if self.head is None:
            self.head=newnode
        else:
            itr=self.head
            while itr.next != None:
                itr=itr.next
            itr.next=newnode        
    def printdata(self):
        if self.head==None:
            print("Link list is empty")
        itr=self.head
        while itr!=None:
            print(f"{itr.data}->")
            itr=itr.next             
ll=linklist()
ll.Insertnode(5)
ll.Insertnode(6)
ll.Insertnode(7)
ll.Insertnode(2)
ll.printdata()













