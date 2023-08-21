import random
import numpy as np
#n rows x m cols
n = 4
m = 4
matrix = [[np.round(random.random(),2) for x in range(m)] for x in range(n)]
# matrix = [[0.0,2.0,3.0],[0.0,5.0,6.0],[7.0,0.0,9.0]]
matrix[0][0] = 0
# print(matrix)


pivots = [0]*n
for i in range(n):
    idx = 0
    for element in matrix[i]:
        if element == 0:
            idx+=1
        else:
            break
    for j in range(i+1,n):
        idy = 0
        for element in matrix[j]:
            if element == 0:
                idy+=1
            else:
                break
        if idy < idx:
            matrix[j],matrix[i] = matrix[i],matrix[j]
            idx = idy
    pivots[i] = idx


matrix = np.array(matrix)
for i in range(n):
    piv = pivots[i];
    pivot_row = matrix[i]
    if pivot_row[piv] != 0:
        for row in matrix[i+1:]:    
            row-= [x*row[piv]/matrix[i][piv] for x in pivot_row];

    for i in range(n):
        idx = 0 
        for element in matrix[i]:
            if element == 0:
                idx+=1
            else:
                break
        pivots[i] = idx










print(matrix)