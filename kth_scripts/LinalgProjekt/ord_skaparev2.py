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

    def split_every_two_words(self):
        self.two_words_list =[]
        for i in range(0, len(self.words)-3):
            self.two_words_list.append(self.words[i] + " " +  self.words[i+1] + " " )#self.words[i+2]+" ")


    def split_every_three_words(self):
        words = self.words
        three_words_list = []
        for i in range(0, len(words)-2):
            three_words_list.append(words[i] + " " + words[i+1] + " " + words[i+2] + " ")
        self.words = three_words_list

    def make_unique(self, list):  # Makes list of all unique words
        uniquel = []
        for word in list:
            if word not in uniquel:
                uniquel.append(word)

        self.uniquel = uniquel  # the unique word list
        dim = len(uniquel)
        self.dim = dim #dimension of transition matrix is equal to dimension the unique word list     

    def make_transmatrix(self, word_list):
        self.matris = [[0.0]*self.dim for x in range(self.dim)]
        for i in range(len(word_list)-1): 
            undex1 = self.uniquel.index(word_list[i])
            undex2 = self.uniquel.index(word_list[i+1])
            self.matris[undex1][undex2] += float(1.0)
        self.matris = np.array(self.matris)
        for row in range(self.matris.shape[0]):
            rowsum = np.sum(self.matris[row])
            if rowsum > 0:
                self.matris[row] /= rowsum
        

    def display(self):
        print(' ', *self.uniquel)
        for i in range(self.dim):
            print(self.uniquel[i], *self.matris[i])
def main2():
    o = analysis()
    o.text_to_list("new_text.txt")
    o.split_every_two_words()
    print(o.two_words_list)

def unique_trans(txt):
    o = analysis()
    o.text_to_list(txt)
    o.split_every_two_words()
    o.make_unique(o.two_words_list)
    #print("Unika ord: Klar\n")

    print(o.uniquel)
    #print(o.words)

    o.make_transmatrix(o.two_words_list)
    #print("Övergångsmatrisen: Klar \n")
    o.display()
    
    return o.uniquel, o.matris

def main():
    unique, trans_matris = unique_trans("gasq.txt") #most important objects to generate is the unique word list and transition matrix
    choices = list(range(len(unique))) #list of indices for the unique list
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
#    print(*mening)
    
main() 
