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
            return str(self.data)+','+str(self.next) #self.next = class(2,null). str(sefl.next) = str(2)+self(null)
        else:
            return str(self.data)

class LinkedQ:
    def __init__(self):
        self.head = None
        

    def isEmpty(self):
        return self.head == None
    
    def add(self, item):
        temp = Node(item) #Temp is now item1,None-------- temp is now item2,None
        temp.setNext(self.head) #Temp is now item1,[None]--------temp is now item2,[item1,None]
        self.head = temp #head is now [item1,None]-------------
    
    def enqueue(self,item):
        if self.head == None:
            self.head = Node(item)
        else:
            x = self.head
            tmp = Node(item)
            while x.getNext() != None:
                x = x.getNext()
            x.setNext(tmp)
    
    
    def dequeue(self):
        tmp = self.head.getData()
        self.head = self.head.getNext()
        return tmp

    def size(self):
        Size = 0
        tmp = self.head
        while tmp != None:
            tmp = tmp.getNext()
            Size+=1
        return Size
    
    def delete(self, pos):
        current = self.head
        previous = None
        index = 0
        
        if current == None:
            return "No item in list"
        
        while index < pos and current != None: #gets the layer "current" where the desired posisition is located. In this case the first layer (4,(blah)) where 4 is data
            previous = current #position updates to current [0] (6,(5,(4,(3,(2,None)))))   [1](5,4,3,2)
            current = current.getNext() #This goes [0](5,4,3,2)  [1](4,3,2)  
            index += 1 #keeps track of how many layers we're in. THe layer will need to be the same as the pos

        if current == None:
            return "No item in list"
        
        else:
            if previous == None: 
                self.head = current.getNext() 
            else:
                current.setNext("blah")
                previous.setNext(current.getNext()) # # # (2,3,4,5,6,7,8) [3]=5 (2,) (4,5,6,7,8).set(6,7,8) -> (4,6,7,8)
                # self.head.setNext(previous) #does nothing. Classes don't copy, they are binded. Altering "previous" also altes the node nested within self.head
                
            return current.getData()
    

    def __str__(self):
        if self.head == None:
            return ''
        else:
            return str(self.head) 
        

# N = LinkedQ()
# N.enqueue(2)
# N.enqueue(3)
# N.enqueue(4)
# N.enqueue(5)



# N.delete(2)

# print(N)


# p = LinkedQ()
# p.enqueue('A')
# p.enqueue('B')
# p.enqueue('C')
# p.enqueue('D')

# q = LinkedQ()
# q.enqueue('E')
# q.enqueue('F')
# q.enqueue('G')



# z = p.head.next
# p.head.next = q.head.next
# z.next.next = p
# q = p = z
# print(p)
