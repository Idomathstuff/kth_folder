graph = {'0': ['1', '2'],
         '1': ['0', '2','3', '4'],
         '2': ['0'],
         '3': ['1'],
         '4': ['2', '3']}

marked = {x:False for x in graph.keys()}
def dfs(graph, start,item):
    print(start)
    # print(marked[item])
    # if marked[item]:
    #     return
    
    marked[start] = True

    for next in graph[start]:
        if not marked[next]:
            dfs(graph, next,item)
    
    return marked



print(dfs(graph,'0','3'))
