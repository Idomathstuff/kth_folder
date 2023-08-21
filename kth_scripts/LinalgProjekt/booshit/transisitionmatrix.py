import numpy as np

class analysis():

    def text_to_list(self,txt): #extracts words from text file
        text_file = open(txt, encoding='utf-8')
        text = text_file.read()
        text = text.lower()
        words = text.split()
        words = [word.strip('.,!;()[]"') for word in words]
        words = [word.strip("'") for word in words]
        words = [word.strip("\\") for word in words]
        words = [word.replace("'s", '') for word in words]

        self.words = words # the word list
        

    def make_unique(self, list): #Makes list of all unique words
        uniquel = []
        for word in list:
            if word not in uniquel:
                uniquel.append(word)
        
        self.uniquel = uniquel #the unique word list
        dim = len(uniquel)
        self.dim = dim

    def make_transmatrix(self,wordl):
        self.matris = [[0.0]*self.dim for x in range(self.dim)] #creates matrix with dimension of the unique list
        for i in range(len(wordl)-1): #Goes through each word in the word list
            undex1 = self.uniquel.index(wordl[i]) #checks index of first word in the unique list
            undex2 = self.uniquel.index(wordl[i+1]) #checks index of follow up word in the unique lsit
            self.matris[undex1][undex2]+=float(1.0) #Adds to the count in row of the first word and col of second word 
        self.matris = np.array(self.matris)  

        for row in range(self.matris.shape[0]): 
            rowsum = np.sum(self.matris[row])
            if rowsum>0:
                self.matris[row] /= rowsum #Divides each row by the sum of its elements

    def display(self):  
        print(' ', *self.uniquel) 
        for i in range(self.dim):
            print(self.uniquel[i], *self.matris[i])



def main(txt):
    o = analysis()
    o.text_to_list(txt)
    o.make_unique(o.words)
    o.make_transmatrix(o.words)
    o.matris = np.around(o.matris, 3)  # Rounds floats in the matrix to 3 decimals


    print(o.words)
#    print(o.uniquel)

    print(o.matris,"\n",
          )
    
    return o.matris, o.uniquel

def trans(txt):
    o = analysis()
    o.text_to_list(txt)
    o.make_unique(o.words)
    o.make_transmatrix(o.words)
    return o.matris


def unique(txt):
    o = analysis()
    o.text_to_list(txt)
    o.make_unique(o.words)
    return o.uniquel

#main("new_text.txt")


trans_matris = trans("navy.txt")
unique = unique("navy.txt")
choices = list(range(len(unique)))


def sentence():

    word1 = "what"
    mening = [word1]
    i=0
    while i<100:
        val = np.random.choice(choices, p=trans_matris[unique.index(mening[i])])
        mening.append(unique[val])
        i+=1
    with open('a_1.txt', 'w') as f:
        for line in mening:
            f.write(line)
            f.write(" ")
    print(*mening)

sentence()

