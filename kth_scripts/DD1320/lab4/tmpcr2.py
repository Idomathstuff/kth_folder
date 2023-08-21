import string
from BintreeFile import Bintree
from lab8.linkedQFile import LinkedQ

file = open("word3.txt", "r", encoding="utf-8").read().split()
svenska = Bintree(file)
gamla = Bintree()

def main():
    slutord_list = []
    startord = input('start ord: ')
    slutord = input('slut ord: ')

    def makechildren(ord,kue):
        gamla.put(ord)
        alfa = string.ascii_letters[:26]+'äåö'
        combinations = []
        for i in range(len(ord)): # // loop that stores all possible combos a word can become in to combinations
            for a in alfa:
                if a == ord[i]:
                    continue
                else:
                    combo = ord[:i]+a+ord[i+1:]
                    combinations.append(combo)
        notaword = [] # // list to check if none of the combos are nodes
        for x in combinations:
            if x in svenska and x not in gamla:
                kue.enqueue(x)
                gamla.put(x) # // stores it in a tree to avoid repeating parents,siblings and children
            else:
                notaword.append(x)
        if notaword == combinations:
            slutord_list.append(ord)

    q=LinkedQ()   
    makechildren(startord,q)
    while not q.isEmpty():
        node = q.dequeue()
        makechildren(node,q)
    if slutord in slutord_list:
        print(startord,' is a slut ord to ',slutord ) 
    else:
        print('Not slut ord')



if __name__ == "__main__":
    main()
    pass
