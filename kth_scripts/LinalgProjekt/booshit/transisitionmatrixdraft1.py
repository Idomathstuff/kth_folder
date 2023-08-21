import numpy as np


l = ['rain', 'rain', 'rain', 'clouds', 'rain', 'sun', 'clouds', 'clouds',
     'rain', 'sun', 'rain', 'rain', 'clouds', 'clouds', 'sun', 'sun',
     'clouds', 'clouds', 'rain', 'clouds', 'sun', 'rain', 'rain', 'sun',
     'sun', 'clouds', 'clouds', 'rain', 'rain', 'sun', 'sun', 'rain',
     'rain', 'sun', 'clouds', 'clouds', 'sun', 'sun', 'clouds', 'rain',
     'rain', 'rain', 'rain', 'sun', 'sun', 'sun', 'sun', 'clouds', 'sun',
     'clouds', 'clouds', 'sun', 'clouds', 'rain', 'sun', 'sun', 'sun',
     'clouds', 'sun', 'rain', 'sun', 'sun', 'sun', 'sun', 'clouds',
     'rain', 'clouds', 'clouds', 'sun', 'sun', 'sun', 'sun', 'sun', 'sun',
     'clouds', 'clouds', 'clouds', 'clouds', 'clouds', 'sun', 'rain',
     'rain', 'rain', 'clouds', 'sun', 'clouds', 'clouds', 'clouds', 'rain',
     'clouds', 'rain', 'sun', 'sun', 'clouds', 'sun', 'sun', 'sun', 'sun',
     'sun', 'sun', 'rain','thunder','thunder']


class analysis():
    def __init__(self):
        self.l =1
    
    def text_to_list(self,txt):
        text_file = open(txt, 'r')
        text = text_file.read()
        text = text.lower()
        words = text.split()
        words = [word.strip('.,!;()[]"') for word in words]
        words = [word.strip("'") for word in words]

        words = [word.replace("'s", '') for word in words]
        self.words = words
        return words

    def unique(self, list):
        uniquel = []
        for word in list:
            if word not in uniquel:
                uniquel.append(word)

        dim = len(uniquel)
        self.matris = [[0.0]*dim for x in range(dim)]
        self.uniquel = uniquel
        self.dim = dim



    def display(self):
        print(' ',*self.uniquel)
        for i in range(self.dim):
            print(self.uniquel[i],*self.matris[i])


    def trans(self,wordl):
        for i in range(len(wordl)-1):
            undex1 = self.uniquel.index(wordl[i])
            undex2 = self.uniquel.index(wordl[i+1])
            self.matris[undex1][undex2]+=float(1.0)
        self.matris = np.array(self.matris)
        for row in range(self.matris.shape[0]):
            rowsum = np.sum(self.matris[row])
            if rowsum>0:
                self.matris[row] /= rowsum

def main():
    k = analysis()
    k.text_to_list("a_1.txt")
    k.unique(k.words)
    k.trans(k.words)
    k.matris = np.around(k.matris, 3)


    print(k.words)
    print(k.uniquel)    
    print(k.matris)




def lorem():
    text_file = open('a_1.txt', 'r')
    text = text_file.read()
    #cleaning
    text = text.lower()
    words = text.split()
    words = [word.strip('.,!;()[]') for word in words]
    words = [word.replace("'s", '') for word in words]

    #finding unique
    unique = []
    for word in words:
        if word not in unique:
            unique.append(word)
    print(unique)

