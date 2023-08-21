import numpy as np
import list_skapare as create


class analysis():
    def text_to_list(self, txt, list_function):  # extracts words from text file        
        self.words = list_function(txt)

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

def unique_trans(txt, list_function):
    o = analysis()
    o.text_to_list(txt, list_function)

    o.make_unique(o.words)
    print("Unika ord: Klar\n")

    o.make_transmatrix(o.words)
    print("Övergångsmatrisen: Klar \n")

    return o.uniquel, o.matris

def calculate_result(mening: list, choices, trans_matris, unique):
    i = len(mening)-1 #starts at upper index of "mening"
    while i < 50: #sentence length limited to 50 words
        val = np.random.choice(choices, p=trans_matris[unique.index(mening[i])])  #spits out a random index of unique words list using the probabilities distribution inside the corresponding row of the word we're trying to follow up on
        mening.append(unique[val]) #adds a unique word indexed in the randomly generated index "val"
        i += 1 #updates the upper index of "mening"

def print_write_result(mening: list, list_function_int: int):
    if list_function_int > 1:
        with open('textpop.txt','w',encoding = 'utf-8') as f: #writing mening in a txt file
            i=1
            for line in mening:
                if i%10 ==0:
                    f.write("\n")
                f.write(line.split()[0])
                f.write(" ")
                i+=1
        print(*mening[::list_function_int])
    else:
        with open('textpop.txt','w',encoding = 'utf-8') as f: #writing mening in a txt file
            i=1
            for line in mening:
                if i%10 ==0:
                    f.write("\n")
                f.write(line)
                f.write(" ")
                i+=1
        print(*mening)

def main():
    list_functions_dict = {0: create.list_one_word, 1: create.list_one_word_wdotcase, 2: create.list_two_words_wdotcase, 3: create.list_three_words_wdotcase}
    list_functions_print_dict = {0: "List with one word", 1: "List with one word and special cases", 2: "List with two words and special cases", 3: "List with three words and special case"}
    
    print(list_functions_print_dict)
    list_function_int = int(input("Välj funktion: "))
    list_function = list_functions_dict[list_function_int]

    unique, trans_matris = unique_trans("new_text.txt", list_function) #most important objects to generate is the unique word list and transition matrix
    choices = list(range(len(unique))) #list of indices for the unique list

    splitting_function_dict = {0: lambda x:x, 1: lambda x:x, 2: create.split_every_two_words, 3: create.split_every_three_words}
    splitting_function = splitting_function_dict[list_function_int]
    start = str(input('Ange några ord: ')) 
    mening = splitting_function(start.split()) #mening becomes list of words
    
    calculate_result(mening, choices, trans_matris, unique)
    print_write_result(mening, list_function_int)

if __name__ == "__main__":
    main()