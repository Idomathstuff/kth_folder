class Node:
    def __init__(self, value): 
        self.value = value
        self.left = None
        self.right = None
    
    def putta(self,item): # // sets one pointer of the tree at a time and gives it a new node with the parent inherting the value at that pointer
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

    def finns(self, item):  # // search algorithim that uitilizes the the binär sökträd is basically identicical to the self.putta() method as it follows parralel to where the searched item would end up
        if self.value == item:
            return True
        else:
            if item <= self.value:
                if self.left == None:
                    return False
                else:
                    return self.left.finns(item)
            else:
                if self.right == None:
                    return False
                else:
                    return self.right.finns(item)
                
    def __str__(self):
        return str(self.value)+': ('+str(self.left)+','+str(self.right)+')'

    def __iter__(self):
        if self.left:
            yield from self.left
        yield self.value
        if self.right:
            yield from self.right


def skriv(root): # // Copied from föreläsning notes

    if root != None:
        skriv(root.left)
        print(root.value),
        skriv(root.right)

class Bintree:
    def __init__(self,root=None): 
        self.root = root

    def put(self,item): 
        if self.root == None:
            self.root = Node(item)
        else:
            self.root.putta(item)

    def __contains__(self, value):
        if self.root == None:
            return False
        else:
            return self.root.finns(value)

    def write(self):
        skriv(self.root)
        
    def __str__(self):
        return str(self.root)
   
    def __iter__(self):
        if self.root.left:
            yield from self.root.left
        yield self.root.value
        if self.root.right:
            yield from self.root.right

tmplist = [7, 5, 4, 3, 2]


def getleft(root):
    tmp = root
    while tmp:
        yield tmp.value
        tmp = tmp.left

def getright(root):
    tmp = root
    while tmp:
        yield tmp.value
        tmp = tmp.right


def test():
    A = Bintree()
    for x in tmplist:
        A.put(x)
    for x in A:
        print(x)


if __name__ == "__main__":
    test()
    pass 

