class Node:
    def __init__(self, dataval):
     self.dataval = dataval
     self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_head(self, dataval):
        new_node = Node(dataval)
        new_node.next = self.head
        self.head= new_node

    def traverse(self):
        n = self.head
        while n is not None:
            print n.dataval,
            n = n.next
            
    def insert_at_end(self, dataval):

        new_node = Node(dataval)

        if self.head is None:
            self.head = new_node
            return

        last=self.head
        while(last.next):
            last=last.next
        last.next=new_node

    
         
L=LinkedList()
L.insert_at_head(10)
L.insert_at_head(20)
L.insert_at_head(30)
L.insert_at_head(40)
L.insert_at_end(50)
L.traverse()
