class Node:
    def __init__(self, initdata):
        self.data = initdata 
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext): 
        self.next = newnext

    def __str__(self): 
        if self.next != None:
            return str(self.data)+' '+str(self.next) # // This __str__ method will be naturally recursive for the linked list since if next is a node it will keep looping this until we have just raw data instead of node classes.
        else:
            return str(self.data) # // If next is None that means we're in the most recent node of the linked queue but we dont want to print the None art so we just print the data.

class LinkedQ:
    def __init__(self): # // Creates self.head instance variable
        self.head = None # // Using the convention thats in the book by using self.head
        self.tail = None
    def isEmpty(self):
        return self.head == None 
    
    def enqueue(self,item):
        if self.head == None:
            self.head = Node(item)
            self.tail = self.head

        else:
            tmp = Node(item) # // initiates a new node with name tmp
            self.tail.next = tmp # // node class is stored in head.next.next
            self.tail = self.tail.next # // tail manipulates its next. Two copies of the same node but only one moves forward. 

    def dequeue(self): # // dequeue removes the very first element in the linkedq by just by head going to its next node through getnext. i.e Equivilant of [1:]
        tmp = self.head.getData()
        self.head = self.head.getNext() 
        return tmp # // Might save the removed data for later

    def size(self): # // LinkedQ Equivlant of len()
        Size = 0
        tmp = self.head
        while tmp != None: # // Keeps going until we reach the last node
            tmp = tmp.getNext() # // Gets tmp to next node
            Size+=1 # // counts up everytime we have another node which is by definition what we want
        return Size

    def __str__(self): 
        return str(self.head)
    





if __name__ == "__main__":
    A = LinkedQ()
    A.enqueue(2)
    A.enqueue(3)
    A.enqueue(4)
    A.enqueue(5)
    print(A)

