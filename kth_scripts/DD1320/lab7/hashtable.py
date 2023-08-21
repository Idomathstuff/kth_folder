class Node:
   def __init__(self, key=None, data=None) -> None:
      self.key = key
      self.data = data
   def __eq__(self, item) -> bool:
       if type(item) == Node :
           return self.key == item.key and self.data == item.data

   def __str__(self) -> str:
       return str(self.key)+':'+str(self.data)

class Hashtable:
    def __init__(self,size):
        self.size = size *10
        self.table = [Node()] * self.size 
        self.krock = 0
        self.keycount = 0

    def store(self,key,data):
        hashvalue = self.hashfunction(key)

        if self.table[hashvalue] == Node()  or self.table[hashvalue].key == key:
            self.table[hashvalue] = Node(key,data)
            self.keycount+=1
            return
        else:
            self.krock +=1
            nextslot = self.rehash(hashvalue)
            while True:
                if self.table[nextslot]== Node():
                    self.table[nextslot] = Node(key, data)
                    self.keycount+=1
                    break
                if self.table[nextslot].key == key:
                    self.table[nextslot] = Node(key, data)
                    self.keycount+=1
                    break
                nextslot = self.rehash(nextslot)
                if nextslot == hashvalue:
                    print('No keys matches',key,'and table is full')
                    break

    
    def search(self,key):
        startslot = self.hashfunction(key)
        stop = False
        found = False
        pos = startslot
        while self.table[pos] != Node() and not found and not stop:
            if self.table[pos].key == key:
                found = True
                data = self.table[pos].data
            else:
                pos = self.rehash(pos)
                if pos == startslot:
                    stop = True
        if found:
            return data
        else:
            raise KeyError

    def hashfunction(self, item):
        if type(item) == str:
            result = 0
            for c in item:
                result *= 100
                result += ord(c)
            return result % self.size
        elif type(item) == int:
            return item % self.size
        
    def rehash(self, item):
        return (item+1) % self.size

    def get_collisions(self):
        print("Collision count: Out of the",self.size,'slots in the table with',self.keycount,'keys...',
              self.krock,'keys need to be probed for.')


    def __getitem__(self,key):
        try:
            return self.search(key)
        except KeyError:
            print('Is not in the table')
    def __setitem__(self,key,data):
        self.store(key,data)
    def __contains__(self,key):
        try:
            self.search(key)
            return True
        except KeyError:
            return False
    def __str__(self) -> str:
        out = '{'
        for x in self.table:
            if x != Node():
                out += str(x.key)+':'+str(x.data)+',\n'
        return out[:-2]+'}'

x = 'hey'

h = Hashtable(len(x))

h.store(x,'lucas')

print(h.search(x))

