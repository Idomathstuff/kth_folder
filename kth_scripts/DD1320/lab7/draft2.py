class Node:
   def __init__(self,key = '',data = None) -> None:
      self.key = key
      self.data = data
   def __eq__(self, item) -> bool:
       return self.key == item
   def __str__(self) -> str:
       return str(self.key)+':'+str(self.data)


def hashfunction(s,size):
    result = 0
    for c in s:
        result *= 100
        result += ord(c)
    return result

class Hashtable:
    def __init__(self,size) -> None:
        self.size = size * 2
        self.table = [None] * self.size 
    
    def hashfunction(self,item):
        if type(item) == str:
            result = 0
            for c in item:
                result*=100
                result+=ord(c)
            return result % self.size
        elif type(item) == int:
            return item % self.size

    def rehash(self, oldhash):
        return (oldhash+1) % self.size
    
    def store(self,key,data):
        
        index = self.hashfunction(key)
        if self.table[index] == None or self.table[index].key == key:
            self.table[index] = Node(key, data)
        else:
            print('finding place for!!!',key)
            next_index = self.rehash(index)
            while self.table[next_index] != None:
                next_index = self.rehash(next_index)
            self.table[next_index] = Node(key,data)

    def search(self,key):
        index = self.hashfunction(key)
        if type(self.table[index]) == Node:
            if self.table[index].key == key:
                return self.table[index].data
            elif self.table[index].key != key:
                raise KeyError
        elif self.table[index] == None:
            raise KeyError

    def __str__(self) -> str:
        out = '{'
        for x in self.table:
            if x!=None:
                out += str(x.key)+':'+str(x.data)+','
        return out[:-1]+'}'

if __name__=='__main__':
    o = Hashtable(10)
    o.store('a','b')
    o.store('c','d')
    print(o.table[19])
    def foo():
        try:
            x = o.search('Zz')
            return True
        except:
            return False

