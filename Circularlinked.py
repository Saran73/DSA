class Node:
    def __init__(self,data):
        self.data=data
        self.ref = None

class Circularlist:
    def __init__(self):
        self.head = None



#TRAVERSAL OPERATION
    def print_CL(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n = self.head
            print(n.data, "---->", end=" ")
            while n.ref is not self.head:
                print(n.data, "---->", end=" ")
                n = n.ref
            # n=self.head
            # while n is not None:
            #     print(n.data,"---->",end=" ")
            #     n = n.ref

#INSERTION OPERATIONS
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node
        self.head.ref = new_node.ref

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n is not None:
                n = n.ref
            n.ref = new_node
            # new_node.ref = self.head

    def add_after_node(self,data,x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n= n.ref
            if n is None:
                print("node is not present in LL")
            else:
                new_node = Node(data)
                new_node.ref = n.ref
                n.ref = new_node




CL1 = Circularlist()
CL1.add_begin(25)
CL1.print_CL()