class Node:
    def __init__(self,data):
        self.data=data
        self.ref=None


class Linkedlist:
    def __init__(self):
        self.head = None


#TRAVERSE LINKED LIST
    def print_LL(self):
        if self.head is None:
            print("linked list is empty")
        else:
            n=self.head
            while n is not None:
                print(n.data,"---->",end=" ")
                n = n.ref


#INSERTING OPERATION
    def add_begin(self,data):
        new_node = Node(data)
        new_node.ref = self.head
        self.head = new_node

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:      
            self.head = new_node
        else:
            n = self.head
            while n.ref is not None:
                n = n.ref
            n.ref = new_node

    def after_node(self,data,x):
        n = self.head
        while n is not None:
            if x == n.data:
                break
            n = n.ref
        if n is None:
            print("node is not present in LL")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

    def before_node(self,data,x):
        if self.head is None:
            print("linked list is empty")
            return
        if self.head.data == x:
            new_node = Node(data)
            new_node.ref = self.head
            self.head = new_node
            return
        n = self.head
        while n.ref is not None:
            if n.ref.data == x:
                break
            n = n.ref

        if n.ref is None:
            print("node not found")
        else:
            new_node = Node(data)
            new_node.ref = n.ref
            n.ref = new_node

#EMPTY LIST OPERATION

    def empty_list(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("not empty")

#DELETE OPERATIONS

    def delete_begin(self):
        if self.head is None:
            print("LL is empty")
        else:
            self.head = self.head.ref

    def delete_end(self):
        if self.head is None:
            print("empty LL ")
        elif self.head.ref is None:
            self.head = None
        else:
            n = self.head
            while n.ref.ref is not None:
                n = n.ref
            n.ref = None

    def delete_by_val(self,x):
        if self.head is None:
            print("empty")
        else:
            if x == self.head.data:
                self.head = self.head.ref
            else:
                n = self.head
                while n.ref is not None:
                    if n == n.ref.data:
                        break
                    n = n.ref
                if n.ref is None:
                    print("node not present")
                else:
                    n.ref=n.ref.ref


LL1 = Linkedlist()
LL1.add_begin(30)
LL1.add_begin(20)
LL1.add_end(40)
LL1.add_end(50)
LL1.delete_by_val(30)
LL1.print_LL()
