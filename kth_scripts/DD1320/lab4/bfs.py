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
        return str(self.parent)+'->'+str(self.item)


def main():
    startord = input('start ord: ')
    while startord not in svenska:
        print("Orden finns inte i ordboken")
        startord = input('Ange start ord igen: ')

    slutord = input('slut ord: ')
    väg_dict = {}
    väg_dict[startord] = startord

    def makechildren(ord, kue):
        gamla.put(ord)
        alfa = string.ascii_letters[:26]+'äåö'
        combinations = []
        # // loop that stores all possible combos a word can become in to combinations
        for i in range(len(ord)):
            for a in alfa:
                if a == ord[i]:
                    continue
                else:
                    combo = ord[:i]+a+ord[i+1:]
                    combinations.append(combo)

        for x in combinations:
            if x in svenska and x not in gamla:
                väg_dict[x] = Node(x)
                väg_dict[x].parent = väg_dict[ord]
                kue.enqueue(x)  # //queues the next batch of children
                # // stores it in a tree to avoid repeating parents,siblings and children
                gamla.put(x)



    # // we need a queue to check if we've gone through all the possible children with the empy method and using deqeue method to systematically go through them all while storing them in gamla.
    q = LinkedQ()
    makechildren(startord, q)
    while not q.isEmpty() and slutord not in gamla:
        node = q.dequeue()
        makechildren(node, q)
    # // because gamla stores every child of the start ord during this process
    if slutord in gamla and slutord != startord:
        print('det finns en väg från', startord, 'till', slutord)
        print(väg_dict[slutord])
    else:
        print('det finns inte en väg till', slutord)





if __name__ == "__main__":
    main()


    pass
