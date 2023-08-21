import timeit


class låt:
    def __init__(self, item) -> None:
        self.trackid = str(item[0])
        self.låttid = str(item[1])
        self.artist = str(item[2])
        self.låttitel = str(item[3])

    def __lt__(self, other):
        return self.artist < other.artist

    def __str__(self) -> str:
        return str(self.artist)+','+str(self.låttitel)


def readfile():
    tmp_list = []
    file = open('unique_tracks.txt', 'r', encoding='utf-8').read().split('\n')
    for x in file:
        låt_object = låt(x.split('<SEP>'))
        tmp_list.append(låt_object)
    return tmp_list


def mergesort(data): # [5,4,3,2,1]
    if len(data) > 1:
        mitten = len(data)//2 # = 2
        vensterHalva = data[:mitten]
        hogerHalva = data[mitten:]

        mergesort(vensterHalva) # mergesort([5,4])
        mergesort(hogerHalva) #mergesort([3,2,1])

        i, j, k = 0, 0, 0

        while i < len(vensterHalva) and j < len(hogerHalva):
            if vensterHalva[i] < hogerHalva[j]:
                data[k] = vensterHalva[i]
                i = i + 1
            else:
                data[k] = hogerHalva[j]
                j = j + 1
            k = k + 1

        while i < len(vensterHalva):
            data[k] = vensterHalva[i]
            i = i + 1
            k = k + 1

        while j < len(hogerHalva):
            data[k] = hogerHalva[j]
            j = j + 1
            k = k + 1

def bubblesort(data):
    n = len(data)
    fortsätt = True
    i = 0
    while fortsätt:
        fortsätt = False
        for j in range(n-1-i):
            if data[j+1] < data[j]:  # jmf
                data[j+1], data[j] = data[j], data[j+1]  # sw
                fortsätt = True
                # for x in data[0:10] :
                    # print(x)
        i += 1
        print(i)

def main():
    lista = readfile()[0:1000]
    lista = readfile()[0:10000]
    lista = readfile()[0:100000]    
    tmp = lista

    bubtid = timeit.timeit(stmt=lambda: bubblesort(lista), number=1)
    print('Bubblesort:', round(bubtid, 4))
    
    mergetid = timeit.timeit(stmt=lambda: mergesort(tmp), number=1)
    print('Mergesort:', round(mergetid, 4))


if __name__=='__main__':
    main()

    
