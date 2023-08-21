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
    
    def enqueue1(self,item): # // Enqueue is a method that puts a node inside the most recent node of a linked queue instance. Equivilant of .append(item)
        if self.head == None: # //  Enqueue will make self.head in to a node. This kicks it off and puts something in head.
            self.head = Node(item) 
        
        else:
            x = self.head # // Since head will the be an object of the Node() class. Assigning it to x will also change the instance variables of head when we setNext in x
            tmp = Node(item) # // This is the node we are going to plant inside the most recent node in the linked Q
            while x.getNext() != None: # // Will keep going until we reach last layer
                x = x.getNext()
            x.setNext(tmp) # // plants the desired value at that node
    
    def enqueue(self,item):
        if self.head == None:
            self.head = Node(item)
            self.tail = self.head
        
        # elif self.tail == None:
        #     tmp = Node(item) # // stores node in tmp
        #     self.head.next = tmp # // next becomes that node class
        #     self.tail = self.head.next# // tail inherits the node

        else:
            tmp = Node(item) # // stores node
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

