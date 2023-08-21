visited = list()
def dfs(graph, start,item=None):
    print(start)
    check = False
    if item in visited:
        check = True
        print(check)
    visited.append(start)


    for next in graph[start]:
        if next not in visited:
            dfs(graph, next)
    return visited


graph = {'0': set(['1', '2']),
         '1': set(['0', '2','3', '4']),
         '2': set(['0']),
         '3': set(['1']),
         '4': set(['2', '3'])}


print(dfs(graph,'2','4'))