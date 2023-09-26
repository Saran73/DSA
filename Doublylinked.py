class Node:
    def __init__(self,data):
        self.data=data
        self.pref = None
        self.nref = None


#TRAVERSE OPERATIONS
class Doubly_linked:
    def __init__(self):
        self.head = None

#FORWARD TRAVERSAL
    def print_LL(self):
        if self.head is None:
            print("linled list is empty")
        else:
            n = self.head
            while n is not None:
                print(n.data, "---->", end=" ")
                n = n.nref

#REVERSE TRAVERSAL
    def print_LL_reverse(self):
        print()
        if self.head is None:
            print("linled list is empty")
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            while n is not None:
                print(n.data, "---->", end=" ")
                n=n.pref

#INSERTION OPERATION
    def insert_empty(self,data):
        if self.head is None:
            new_node = Node(data)
            self.head = new_node
        else:
            print("linked list not empty")

    def add_begin(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            new_node.nref = n
            n.pref = new_node
            self.head = new_node

    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.nref is not None:
                n = n.nref
            n.nref = new_node
            new_node.pref = n

    def add_after(self,data,x):
        if self.head is None:
            print("linked list is empty!!")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("node is not present!!")
            else:
                new_node = Node(data)
                new_node.nref = n.nref
                new_node.pref = n
                if n.nref is not None:
                    n.nref.pref = new_node
                n.nref = new_node

    def add_before(self,data,x):
        if self.head is None:
            print("linked list is empty!!")
        else:
            n = self.head
            while n is not None:
                if x == n.data:
                    break
                n = n.nref
            if n is None:
                print("node is not present!!")
            else:
                new_node = Node(data)
                new_node.nref = n
                new_node.pref = n.pref
                if n.pref is not None:
                    n.pref.nref = new_node
                else:
                    self.head = None
                n.pref = new_node

#DELETION OPERATION
    def delete_begin(self):
        if self.head is None:
            print("DLL is empty ")
        else:
            if self.head.nref is None:
                self.head = None
                print("DLL is empty after deleting node")
            else:
                self.head = self.head.nref
                self.head.pref = None

    def delete_end(self):
        if self.head is None:
            print("DLL is empty")
        else:
            if self.head.nref is None:
                self.head = None
                print("DLL is empty after deleting node")
            else:
                n = self.head
                while n.nref is not None:
                    n = n.nref
                n.pref.nref = None

    def delete_by_val(self,x):
        if self.head is None:
            print("DLL is empty")
        else:
            if self.head.nref is None:
                if x == self.head.data:
                    self.head = None
                else:
                    print("Given node is not present!")
            else:
                if self.head.data == x:
                    self.head = self.head.nref
                    self.head.pref = None
                n =self.head
                while n.nref is not None:
                    if x == n.data:
                        break
                    n = n.nref
                if n.nref is not None:
                    n.nref.pref = n.pref
                    n.pref.nref = n.nref
                else:
                    if n.data==x:
                        n.pref.nref = None
                    else:
                        print("DLL is not present")







DL1 = Doubly_linked()
DL1.add_begin(4)
DL1.add_after(10,4)
DL1.add_before(25,10)
DL1.delete_by_val(25)
DL1.print_LL()
#DL1.print_LL_reverse()