import sys
from BintreeFile import Bintree
from lab8.linkedQFile import LinkedQ

class Vertex:   
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectedTo[nbr] = weight # // 

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo]) # // 

    def getConnections(self):
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        return self.connectedTo[nbr]


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        self.numVertices = self.numVertices + 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        if n in self.vertList:
            return self.vertList[n]
        else:
            return None

    def __contains__(self, n):
        return n in self.vertList

    def addEdge(self, f, t, weight=0):
        if f not in self.vertList:
            nv = self.addVertex(f)
        if t not in self.vertList:
            nv = self.addVertex(t)
        self.vertList[f].addNeighbor(self.vertList[t], weight)

    def getVertices(self):
        return self.vertList.keys()
    def __str__(self) -> str:
        self.vertList = dict(sorted(self.vertList.items(), key=lambda x: x[0]))
        for key in self.vertList:
            print(self.vertList[key])
    def __iter__(self):
        return iter(self.vertList.values())

def tmp():
    # tmp = Vertex(0)
    # tmp.addNeighbor(Vertex(1),3)
    # tmp.addNeighbor(Vertex(2),1)
    # print(tmp)
    # // tmp.addneighbor(Verte)
    # // 
    # //
    # //
    # //
    # //
    B = Graph()
    B.addVertex(1)
    B.addVertex(2)
    B.addVertex(3)
    B.addEdge(1,2,5)
    B.addEdge(2, 1, 5)
    B.addEdge(2, 3, 5)
    B.addEdge(3, 2, 5)
    try:
        print(B)
    except:
        pass
    pass


import string
file = open("word3.txt", "r", encoding="utf-8").read().split()
svenska = Bintree(file)



slutord_lista = []
def makechildren(ord,kue):
    gamla = Bintree()
    alfa = string.ascii_letters[:26]+'äåö'
    bucket = []
    for i in range(len(ord)):
        for a in alfa:
            if a==ord[i]:
                continue
            else:
                combo = ord[:i]+a+ord[i+1:]
                bucket.append(combo)
    # kue = LinkedQ()
    for x in bucket:
        if x in svenska and x not in gamla:
            kue.enqueue(x)
            # print(x,end=' ')
            gamla.put(x)
        # elif not x in svenska:
        #     slutord_lista.append(ord)


def start():
    startord = 'söt' #input()
    # slutord = input()
    
    q = LinkedQ
    makechildren(startord,q)
    # while not q.isEmpty():
    #     nod = q.dequeue()
    #     makechildren(nod,q)



if __name__ == "__main__":
    # tmp()
    start()
    print(slutord_lista)
    pass
