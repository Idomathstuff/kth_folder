import numpy as np


class analysis():
    def text_to_list(self, txt):  # extracts words from text file
        text_file = open(txt,'r', encoding='utf-8')
        text = text_file.read()
        text = text.lower()
        words = text.split()
        words = [word.strip('.,!;()[]"') for word in words]
        words = [word.strip("'") for word in words]
        words = [word.strip("\\") for word in words]
        words = [word.replace("'s", '') for word in words]
        self.words = words  # the word list of txt file

    def make_unique(self, list):  # Makes list of all unique words
        uniquel = []
        for word in list:
            if word not in uniquel:
                uniquel.append(word)
        self.uniquel = uniquel  # the unique word list
        dim = len(uniquel)
        self.dim = dim #dimension of transition matrix is equal to dimension the unique word list

    def make_transmatrix(self, wordl):
        # creates matrix with dimension of the unique list
        self.matris = [[0.0]*self.dim for x in range(self.dim)]
        for i in range(len(wordl)-1):  # Goes through each word in the word list
            # checks index of first word in the unique list
            undex1 = self.uniquel.index(wordl[i])
            # checks index of follow up word in the unique lsit
            undex2 = self.uniquel.index(wordl[i+1])
            # Adds to the count in row of the first word and col of second word
            self.matris[undex1][undex2] += float(1.0)
        self.matris = np.array(self.matris)

        for row in range(self.matris.shape[0]):
            rowsum = np.sum(self.matris[row])
            if rowsum > 0:
                # Divides each row by the sum of its elements
                self.matris[row] /= rowsum

        



def unique_trans(txt):
    o = analysis()
    o.text_to_list(txt)

    o.make_unique(o.words)
    print("Unika ord: Klar\n")

    o.make_transmatrix(o.words)
    print("Övergångsmatrisen: Klar \n")


    return o.uniquel, o.matris


def main():
    # most important objects to generate is the unique word list and transition matrix
    unique, trans_matris = unique_trans("new_text.txt")


    choices = list(range(len(unique)))  # list of indices for the unique list
    start = str(input('Ange några ord: ')) 
    mening = start.split() #mening becomes list of words
    i = len(mening)-1 #starts at upper index of "mening"
    while i < 50: #sentence length limited to 50 words
        val = np.random.choice(choices, p=trans_matris[unique.index(mening[i])])  #spits out a random index of unique words list using the probabilities distribution inside the corresponding row of the word we're trying to follow up on
        mening.append(unique[val]) #adds a unique word indexed in the randomly generated index "val"
        i += 1 #updates the upper index of "mening"
    with open('textpop.txt','w',encoding = 'utf-8') as f: #writing mening in a txt file
        i=1
        for line in mening:
            if i%10 ==0:
                f.write("\n")
            f.write(line)
            f.write(" ")
            i+=1
    print(*mening)




main()
