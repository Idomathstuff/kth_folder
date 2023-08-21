import array
import random

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


class Stack:
    def __init__(self):
         self.items = []

    def isEmpty(self):
         return self.items == []

    def push(self, item):
         self.items.append(item)

    def pop(self):
         return self.items.pop()

    def peek(self):
         return self.items[len(self.items)-1]

    def size(self):
         return len(self.items)


# "Trollkarlen tar ut de tretton spaderna ur deck, håller dem som en
# kortlek med baksidan upp och lägger ut dem på följande sätt: Översta
# kortet stoppas underst, nästa kort läggs ut med framsidan upp, nästa
# kort stoppas underst, nästa kort läggs ut osv.  Till publikens
# häpnad kommer korten upp i ordning ess, tvåa, trea...
# Utförande: Man ordnar i hemlighet korten enligt följande: "
# Ö -> U
# 3   1   4   2   5
# [1   4   2   5 3]
# [4   2   5 3] 1
# [2   5 3 4] 1
#[5 3 4] 1 2
# [345]
#45 123
#54 123

class ArrayQ:
    def __init__(self):
        self.arr = array.array('b',[])

    def enqueue(self,input):
        self.arr.append(input)

    def dequeue(self):
        tmp = self.arr[0]
        self.arr.pop(0)
        return int(tmp)
    
    def size(self):
        return len(self.arr)
    
    def isEmpty(self):
        if self.size() == 0:
            return True
        else:
            return False

    def __str__(self):
        return str(list(self.arr))





def card_list(n):
    A = list(range(1,n+1))
    random.shuffle(A)
    return A


def main():
    deck = ArrayQ()
    out_deck = ArrayQ()
    svar = None

    while True:
        svar = input("Lägg ett kort på deck. Om du är klar ange 'y' ")
    
        if svar == 'y':
            break
        if svar == '':
            deck = ArrayQ()
            deck.enqueue(3)
            deck.enqueue(1)
            deck.enqueue(4)
            deck.enqueue(2)
            deck.enqueue(5)
            break
        deck.enqueue(int(svar))
    
    while deck.isEmpty() == False:
        
        tmp1 = deck.dequeue()
        deck.enqueue(tmp1)

        tmp2 = deck.dequeue()
        out_deck.enqueue(tmp2)

    print(deck, out_deck)
        
def foo():
    pass
k = [main, foo]

if __name__=="__main__":
    A = array.array('b',[])
    main()
    pass



# ctrl + '
# ctrl + up/down shifts line up or down
# ctrl + l
