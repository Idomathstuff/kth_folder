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
            tmp = Node(item)  # // stores node
            self.tail.next = tmp  # // node class is stored in head.next.next
            # // tail manipulates its next. Two copies of the same node but only one moves forward.
            self.tail = self.tail.next
        self.size += 1

    # // dequeue removes the very first element in the linkedq by just by head going to its next node through getnext. i.e Equivilant of [1:]
    def dequeue(self):
        tmp = self.head.data
        self.head = self.head.next
        self.size -= 1
        return tmp  # // Might save the removed data for later

    def peek(self):
        if not self.isEmpty():
            return self.head.data
        else:
            return None

    def __str__(self):
        return str(self.head)


if __name__ == "__main__":
    A = LinkedQ()
    A.enqueue(2)
    A.enqueue(3)
    A.enqueue(4)
    A.enqueue(5)
    print(A)
