class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self,data):
        if self.key is None:
            self.key = data
        else:
            if self.key == data:
                return
            if self.key > data:
                if self.lchild:
                    self.lchild.insert(data)
                else:
                    self.lchild = BST(data)
            else:
                if self.rchild:
                    self.rchild.insert(data)
                else:
                    self.rchild = BST(data)


    def search(self,data):
        if self.key == data:
            print("Node is found")
        else:
            if data < self.key:
                if self.lchild:
                    self.lchild.search(data)
                else:
                    print("Node is not present!")
            else:
                if self.rchild.search:
                    self.rchild.search(data)
                else:
                    print("Node is not present!!!")


    def pre_order(self):
        print(self.key,end=" ")
        if self.lchild:
            self.lchild.pre_order()
        if self.rchild:
            self.rchild.pre_order()

    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key,end=" ")
        if self.rchild:
            self.rchild.inorder()

    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key,end=" ")

    def delete(self,data,curr):
        if self.key is None:
            print("BST IS EMPTY")
            return
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data,curr)
            else:
                print("Node is not present in tree")
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data,curr)
            else:
                print("Node is not present in tree")
        else:
            if self.lchild is None:
                temp = self.rchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self = None
                return temp
            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key,curr)
        return self

    def min_node(self):
        current = self
        while current.lchild:
            current = current.lchild
        print("node with smallest key is: ",current.key)

    def max_node(self):
        current = self
        while current.rchild:
            current = current.rchild
        print("node with Maximum key is: ", current.key)



def count(node):
    if node is None:
        return 0
    return 1+count(node.lchild)+count(node.rchild)







root = BST(10)
list1 = [3,4,7,23,76,10]
for i in list1:
    root.insert(i)
print(count(root))
root.pre_order()
print("Preorder")
if count(root)>1:
    root.delete(10,root.key)
else:
    print("Can't perform deletion")
print("after deleting")
root.pre_order()
print()
root.min_node()
root.max_node()