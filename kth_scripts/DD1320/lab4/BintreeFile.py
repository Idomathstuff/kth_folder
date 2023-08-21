class Node:
    def __init__(self, value): # // cited from book/föreläsning
        self.value = value 
        self.left = None
        self.right = None
    
    def __str__(self): # // method that I made to see that the nodes are in the right place
        return str(self.value)+': ('+str(self.left)+','+str(self.right)+')'

    def __iter__(self): 
        if self.right:
            yield from self.right
        yield self.value
        if self.left:
            yield from self.left

def putta(root, item): # // Hjälp funktion that I made. It checks a node if its pointers are filled or not to add another node. It recursively goes to the next node otherwise.
    if item <= root.value:
        if root.left == None:
            root.left = Node(item)
        else:
            putta(root.left, item)
    else:
        if root.right == None:
            root.right = Node(item)
        else:
            putta(root.right,item)

def finns(p, value): # // Hjälp funktion copied from föreläsning anteckningar
    if p == None:
        return False
    if value == p.value:
        return True
    if value < p.value:
        return finns(p.left, value)
    if value > p.value:
        return finns(p.right, value)


def skriv(root):  # // Hjälp funktion Copied from föreläsning notes
    if root != None:
        skriv(root.left)
        print(root.value),
        skriv(root.right)

class Bintree:
    def __init__(self,item=None): 
        self.root = None
        if type(item) is list:
            self.put(item)
        else:
            self.root = item

    def put(self,item): 
        if type(item) is list:
            for x in item:
                if self.root == None:
                    self.root = Node(x)
                else:
                    putta(self.root,x)
        else:
            if self.root == None:
                self.root = Node(item)
            else:
                putta(self.root, item)
                        

    def write(self):
        skriv(self.root)

    def __contains__(self, value):
        return finns(self.root,value)
        
    def __str__(self):
        return str(self.root)

    def __iter__(self):
        if self.root.right:
            yield from self.root.right
        yield self.root.value
        if self.root.left:
            yield from self.root.left



def test():
    svenska = Bintree()
    engelska = Bintree()
    file = open("engelska.txt", "r", encoding="utf-8").read().lower().split()
    file = [word.strip('",. ') for word in file]
    
    with open("word3.txt", "r", encoding="utf-8") as svenskfil:
        for rad in svenskfil:
            ordet = rad.strip()                # Ett trebokstavsord per rad
            if ordet in svenska:
                print(ordet, end=" ")
            else:
                svenska.put(ordet)             # in i sökträdet
    print("\n")

    for ord in file:
        if ord in engelska:
            pass #gör igenting
        else:
            engelska.put(ord)
            if ord in svenska:
                print(ord, end=" ")


if __name__ == "__main__":
    test()
    pass 

