import sys

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
    def getRight(self):
        return self.right
    def getLeft(self):
        return self.left

    def setRight(self,item):
        self.right = item
    
    def setLeft(self,item):
        self.left = item

    def set(self,item1,item2):
        self.right, self.left = item1, item2

    def isleaf(self):
        if self.right==None and self.left == None:
            return True
        

    def exists(self, item):
        if self.value == item:
            return True
        else:
            if item<=self.value:
                if self.left == None:
                    return False
                else:
                    return self.left.exists(item)
            else:
                if self.right == None:
                    return False
                else:
                    return self.right.exists(item)
    
    def putta(self,item):
        if item <= self.value:
            if self.left == None:
                self.left = Node(item)
            else:
                self.left.putta(item)
        else:
            if self.right == None:
                self.right = Node(item)
            else:
                self.right.putta(item)
            

    def __str__(self):

        return str(self.value)+': ('+str(self.left)+','+str(self.right)+')'


# def putta(node,item: int):
#     if item<=node.value:
#         if node.left==None:
#             node.setLeft(Node(item))
#         else:
#             putta(node.left,item)
#     else:
#         if node.right == None:
#             node.setRight(Node(item))
#         else:
#             putta(node.right,item)


# def finns(node,item):
#     if node.value == item:
#         return True
#     else:
#         if item <= node.value:
#             if node.left == None:
#                 return False
#             else:
#                 return finns(node.left,item)
#         else:
#             if node.right == None:
#                 return False
#             else:
#                 return finns(node.right,item)

class Bintree:
    def __init__(self,root=None):
        self.root = root

    def put(self,item):
        if self.root == None:
            self.root = Node(item)
        else:
            self.root.putta(item)

    def __contains__(self, value):
        return self.root.exists(value)

    def write(self):
        print(self.root)

    def __str__(self):
        return str(self.root)
    

def make_tree():
    A=Bintree()
    svar = sys.stdin.readline()
    for x in svar.split():
        if x != ' ' and x != '\n':
            A.put(x)
    print(A)




# import numpy as np
# def f(n):
#     m = np.array([[1,1],[1,0]])
#     v = np.array([1,0])
#     m = np.linalg.matrix_power(m,n-1)
#     return np.dot(m,v)


if __name__ == "__main__":
    # make_tree()
    # print("AB"<"AA")
    pass 

