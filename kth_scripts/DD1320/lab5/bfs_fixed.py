import string
from BintreeFile import Bintree
from lab8.linkedQFile import LinkedQ

file = open("word3.txt", "r", encoding="utf-8").read().split()

svenska = Bintree(file)
gamla = Bintree()

class Node:
    def __init__(self, item) -> None:
        self.parent = None
        self.item = item
    def __str__(self) -> str:
        if self.parent: 
            return str(self.parent)+'->'+str(self.item) # // where the recursion occours
        else:
            return str(self.item)
def main():
    startord = input('start ord: ')
    while startord not in svenska:
        print("Orden finns inte i ordboken")
        startord = input('Ange start ord igen: ')
    slutord = input('slut ord: ')


    def makechildren(node, kue): 
        ord = node.item
        gamla.put(ord)
        alfa = string.ascii_letters[:26]+'äåö'
        combinations = []
        for i in range(len(ord)):
            for a in alfa:
                if a == ord[i]:
                    continue
                else:
                    combo = ord[:i]+a+ord[i+1:]
                    combinations.append(combo)
        for x in combinations:
            if x in svenska and x not in gamla:
                tmp = Node(x)
                tmp.parent = node
                kue.enqueue(tmp)  

                gamla.put(x)

    q = LinkedQ()
    makechildren(Node(startord), q)

    while not q.isEmpty():        
        node = q.dequeue()
        if node.item == slutord:
            break
        makechildren(node, q)
    
    if slutord in gamla and slutord != startord:
        print('det finns en väg från', startord, 'till', slutord)
        print(node)
    else:
        print('det finns inte en väg till', slutord)

if __name__ == "__main__":
    main()
    pass
