import array

class ArrayQ:
    def __init__(self):
        self.arr = array.array('h', [])

    def enqueue(self, input):
        self.arr.append(input)

    # def dequeue(self):
    #     tmp = self.arr[0]
    #     self.arr.pop(0)
    #     return int(tmp)

    def size(self):
        return len(self.arr)

    def isEmpty(self):
        if self.size() == 0:
            return True
        else:
            return False

    def __str__(self):
        return str(list(self.arr))
        
