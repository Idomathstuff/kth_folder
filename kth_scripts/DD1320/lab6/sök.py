import timeit 
class låt:
    def __init__(self,item) -> None:
        self.trackid = str(item[0])
        self.låttid = str(item[1])
        self.artist = str(item[2])
        self.låttitel = str(item[3])
    def __lt__(self,other):
        if type(other) == låt:
            return self.artist < other.artist
        elif type(other) == str:
            return self.artist < other
        
    def __gt__(self,other):
        if type(other) == låt:
            return self.artist > other.artist
        elif type(other) == str:
            return self.artist > other
        
    def __eq__(self, other) -> bool:
        if type(other) == låt:
            return self.artist == other.artist
        elif type(other) == str:
            return self.artist == other
        

    def __str__(self) -> str:
        return str(self.artist)+','+str(self.låttitel)


def readfile():
    tmp_list = []
    file = open('unique_tracks.txt','r',encoding='utf-8').read().split('\n')
    for x in file:
        låt_object = låt(x.split('<SEP>'))
        tmp_list.append(låt_object)
    return tmp_list

def linsok(lista,item):
    for x in lista:
        if x==item:
            return True



def binarsok(lista,item):
    # lista = sorted(lista,key=lambda x: x)
    

    tmpl = lista
    found = False
    l = 0
    u = len(tmpl)-1
    while l<=u:
        # print(l,u)
        mid = (l+u)//2
        tmpm = tmpl[mid]
        if tmpm == item:
            return True
        else:
            if item < tmpm:
                u = mid;
            elif item > tmpm:
                l = mid;
    return False

def hashsok(table,item):
    try:
        return table[item]
    except:
        return False


def main():
    sista = 'Muse'
    lista = readfile()[0:250000] 
    # lista = readfile()[0:2*250000]
    # lista = readfile()[0:4*250000]
    n = len(lista)


    print("Antal element =", n)
    linjtid = timeit.timeit(stmt=lambda: linsok(lista, sista), number = 1)
    print("Linjärsökningen:", round(linjtid, 4))

    lista = sorted(lista, key = lambda x:x.artist)

    bintid = timeit.timeit(stmt=lambda: binarsok(lista, sista), number=1)
    print("Binärsökning:",round(bintid,6))
    table = {x.artist: True for x in lista}
    hashtid = timeit.timeit(stmt = lambda: hashsok(table,sista),number =1)
    print('Hashsökning:',round(hashtid,4))


if __name__=='__main__':
    main()