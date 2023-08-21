from hashtable import Hashtable

class pokemon:
    def __init__(self,line) -> None:
        self.show = line
        line = line.split(',')
        self.name = line[1]
        self.type1 = line[2]

        if line[3] =='':
            self.type2 = None
        else:
            self.type2 = line[3]
        self.total = line[4]
        self.attack = line[5]
        self.defense = line[6]
        self.spattack = line[7]
        self.spdefense = line[8]
        self.speed = line[9]
        self.generation = line[10]
        self.legendary = line[11]
    def __str__(self) -> str:
        return self.show


def main():
    file = open('pokemon.csv','r',encoding='utf-8').read().split('\n')[:10]
    poketable = Hashtable(len(file))
    for poke in file:
        try:
            temp = pokemon(poke)
            poketable.store(temp.name,temp)
        except:
            pass
    print('Charmander in poketable:','Charmander' in poketable)
    print('Big boy in poketable:', 'Big boy' in poketable)

if __name__=='__main__':
    main()


