from sys import stdin


def hash2(s):
    result = 0
    for c in s:
        result *= 100
        result += ord(c)
    return result


class Node:
  def __init__(self, key="", data=None):
      """key: nyckeln som anvands vid hashningen
        data: det objekt som ska hashas in"""
      self.key = key
      self.data = data


class HashTable:
    def __init__(self,size):
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def store(self, key, data):
      hashvalue = self.hashfunction(key, len(self.slots)) # gives an index number to a given key

      if self.slots[hashvalue] == None: #put in 
        self.slots[hashvalue] = key
        self.data[hashvalue] = data
      else:
        if self.slots[hashvalue] == key: #replaces if the index matches the hash
          self.data[hashvalue] = data  
        else:
          nextslot = self.rehash(hashvalue, len(self.slots)) #collision since the index matches but not the key
          while self.slots[nextslot] != None and \
                  self.slots[nextslot] != key:
            nextslot = self.rehash(nextslot, len(self.slots))

          if self.slots[nextslot] == None:
            self.slots[nextslot] = key
            self.data[nextslot] = data
          else:
            self.data[nextslot] = data  # replace

    def hashfunction(self, key, size):
        if type(key) == str:
           return hash2(key) % size
        else:
         return key % size

    def rehash(self, oldhash, size):
        return (oldhash+1) % size

    def search(self, key):
      startslot = self.hashfunction(key, len(self.slots))

      data = None
      stop = False
      found = False
      position = startslot
      while self.slots[position] != None and  \
              not found and not stop:
         if self.slots[position] == key:
           found = True
           data = self.data[position]
         else:
           position = self.rehash(position, len(self.slots))
           if position == startslot:
               stop = True
      if data == None:
         raise KeyError
      return data


    def __getitem__(self, key):
        return self.search(key)

    def __setitem__(self, key, data):
        self.store(key, data)
    def __str__(self) -> str:
       return str(self.slots)+'\n'+str(self.data)




def main():
    hashtable = HashTable(150001)

    for line in stdin:
        line = line.strip()
        key, *value = line.split()
        if key == '#':
            break
        elif len(value) != 0:
            hashtable.store(key, value[0])
        else:
            try:
                value = hashtable.search(key)
                print(value)
            except KeyError:
                print('None')
    print(hashtable)


if __name__ == "__main__":
    main()
