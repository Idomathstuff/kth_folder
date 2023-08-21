class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def __str__(self):
        if self.next != None:
            # // This __str__ method will be naturally recursive for the linked list since if next is a node it will keep looping this until we have just raw data instead of node classes.
            return str(self.data)+''+str(self.next)
        elif self.next == None:
            # // If next is None that means we're in the most recent node of the linked queue but we dont want to print the None art so we just print the data.
            if str(self.data) == None:
                return ""
            else:
                return str(self.data)
class LinkedQ:
    def __init__(self):  # // Creates self.head instance variable
        self.head = None  # // Using the convention thats in the book by using self.head
        self.tail = None
        self.size = 0

    def isEmpty(self):
        return self.head == None

    def enqueue(self, item):
        if self.head == None:
            self.head = Node(item)
            self.tail = self.head
        else:
            tmp = Node(item)  
            self.tail.next = tmp  
            self.tail = self.tail.next
        self.size += 1

    def dequeue(self):
        if self.size != 0:
            tmp = self.head.data
            self.head = self.head.next
            self.size -= 1
            return tmp 
        else:
            return None

    def peek(self):
        # if not self.isEmpty():
        #     return self.head.data
        # else:
        #     return None
        try:
            return self.head.data
        except AttributeError:
            return None
    def __len__(self):
        return self.size
    def __str__(self):
        if type(self.head) == Node:
            if self.head.data == None:
                return ""
            return str(self.head)
        elif self.head == None:
            return ""


if __name__ == "__main__":
    A = LinkedQ()
    A.enqueue(2)
    A.enqueue(3)
    A.enqueue(4)
    A.enqueue(5)
    A.dequeue()
    A.dequeue()
    A.dequeue()
    A.dequeue()
    print(A)
