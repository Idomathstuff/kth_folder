from lab8.linkedQFile import LinkedQ
def str_get_freq(sträng: str):
    freq = {}
    sträng = sträng.replace(' ','')
    for x in sträng:
        freq[x]=0
    for x in sträng:
        freq[x]+=1

    return freq

freq = str_get_freq('sadfasdfasdfasscasdcsadfssadasdasdgretijqehrqilwnciuwnqecqwad')
freq = dict(sorted(freq.items(),key = lambda x: x[1])) 
char_list = list(freq.keys())


class node:
    def __init__(self,item) -> None:
        self.parent = None
        self.item = item
    def __str__(self) -> str:
        if self.parent is not None:
            return str(self.item) + '->' + str(self.parent)
        else:
            return str(self.item)


class treenode:
    def __init__(self,value) -> None:
        self.parent = None
        self.value = value
        self.left = None
        self.right = None

foo = LinkedQ()

barn_node = {}
for x in char_list:
    barn_node[x] = node(x)

def hashtree1():
    barn_node[char_list[0]].parent = node(freq[char_list[0]]+freq[char_list[1]])
    barn_node[char_list[1]].parent = barn_node[char_list[0]].parent
    tmp0 = barn_node[char_list[0]].parent
    for x in char_list[2:]:
        if freq[x] < tmp0.item:
            tmp1 = node(freq[x]+tmp0.item)
            tmp0.parent = tmp1
            barn_node[x].parent = tmp1
            tmp0 = tmp1

def hashtree():
    barn_node[char_list[0]].parent = treenode()


# hashtree1()
# for x in barn_node.keys():
#     print(barn_node[x])

def compress(uncompressed):
    """Compress a string to a list of output symbols."""

    # Build the dictionary.
    dict_size = 256
    dictionary = dict((chr(i), i) for i in range(dict_size))
    # in Python 3: dictionary = {chr(i): i for i in range(dict_size)}

    w = ""
    result = []
    for c in uncompressed:
        wc = w + c
        if wc in dictionary:
            w = wc
        else:
            result.append(dictionary[w])
            # Add wc to the dictionary.
            dictionary[wc] = dict_size
            dict_size += 1
            w = c

    # Output the code for w.
    if w:
        result.append(dictionary[w])
    return result

# print(compress('blablaba'))

import re
pattern="[Ll]abb? ?[1-8]"
sometext="Lab5, labb 6, labb7 och lab8"
print(re.findall(pattern,sometext))