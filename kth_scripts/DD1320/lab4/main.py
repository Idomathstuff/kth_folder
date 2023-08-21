# // Problemet: Avgör om det finns en väg från ett ord till ett annat ord  
# // make adjacency matrix

from temp import Graph

def buildGraph(wordFile):
    d = {}
    g = Graph()
    wfile = open(wordFile, 'r',encoding = "utf-8")
    # create buckets of words that differ by one letter
    for line in wfile:
        word = line[:-1] # // deletes last letter in line
        for i in range(len(word)): 
            bucket = word[:i] + '_' + word[i+1:] # // outputs s_r
            if bucket in d:
                d[bucket].append(word) # // more elements in s_r
            else:
                d[bucket] = [word] # // first element in s_r
    # add vertices and edges for words in the same bucket

    for bucket in d.keys(): 
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word2) # // Connects every single element in bucket s_r 
    return g


# a = {'b': {'bar':'foo1'}, 'a': 'bar2', 'foo3': 'bar3',
#      'foo4': 'bar4', 'foo5': 'bar5', }
# k = sorted(a.items(),key=lambda x: x[0])
# print(dict(k))
# for x in k:
#     print(x)
# for i in range(len('dock')):
#     print('dock'[:i]+'_'+'dock'[i+1:])



graf = buildGraph('word3.txt')
try:
    print(graf)
except:
    pass















if __name__== "__main__":
    pass 