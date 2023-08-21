from random import randint as rand
import numpy as np
import sympy
#b = [[rand(0,10) for x in range(3)] for y in range(3)]   #equivlant of np.arange(1,10).reshape(3,3)

#b = np.arange(1,10).reshape(3,3)

#print(b)
#print(np.array(b))


'''def first_pivot(matrix):
    non_zero_row = '' 
    data = list()
    min_0 = matrix[0].count(0)
    listt = list()
    for row in matrix:
        pos = 0
        for x in row:
            if x != 0:
                listt.append(pos)
                break
            pos += 1
    pos = 0
    for row in matrix:
        if listt[pos] == min(listt) and row.count(0) <= min_0:
            non_zero_row = row
        min_0 = row.count(0)
        pos +=1
    data.append(non_zero_row)
    data.append(pos-1)
    return data
'''

#np.random.random((4,4))
'''x = 0
for i in b:
    print(first_pivot(b)[0])
    b.pop(first_pivot(b)[1]-x)
    if len(b) == 1:
        print(b[0])
        break
    x+=1

'''
def ToReducedRowEchelonForm(M):
    if not M:
        return
    lead = 0
    rowCount = len(M)
    columnCount = len(M[0])
    for r in range(rowCount):
        if lead >= columnCount:
            return
        i = r
        while M[i][lead] == 0:
            i += 1
            if i == rowCount:
                i = r
                lead += 1
                if columnCount == lead:
                    return
        M[i], M[r] = M[r], M[i]
        lv = M[r][lead]
        M[r] = [mrx / float(lv) for mrx in M[r]]
        for i in range(rowCount):
            if i != r:
                lv = M[i][lead]
                M[i] = [iv - lv*rv for rv, iv in zip(M[r], M[i])]
        lead += 1


#ToReducedRowEchelonForm(b)

#print(np.array(b))

#print(list(zip([1,2,3,4],[5,6,7,8])))
'''

x = 'a'
lista = '['

def func(x):
    return round((x**2)/15 + 6*x/15-3*np.sin(5*x/2 +1)/5 +1, 3)

for n in range(25):
    x = 'f(' + x +')'
    lista = lista + ','+x

lista += ']'

print(lista)

'''
b = [
    [0,0,3,-1],
    [0,0,0,1],
    [0,0,9,5],
    [0,0,1,3]]

matrix = b

n = len(matrix) #matrix height
m = len(matrix[0]) #row length
def ech():
        for i in range(n):
            row=0
            state = True
            while state == True:
                if matrix[row][i] !=0:
                    matrix[row],matrix[i] = matrix[i],matrix[row]
                    state = False
                    row = 0
                else:
                    row+=1

def ech2(): #flaw is that it only checks pivots along the diagonal 
    for col in range(m):
        row = 0
        pivot = matrix[col][col]
        while row < 4 and pivot == 0:
            print("Coords:",row,col)
            print("pivot value in:",col,col,"=",pivot)
            pivot = matrix[col][col]
            if matrix[row][col] != 0:
                matrix[row],matrix[col] = matrix[col], matrix[row]
                print(np.array(matrix),"\n")
            else:
                row += 1

            print(pivot)
            
    print("done here: \n", np.array(matrix))    
    
def firstpivot():
    check = 0
    row = 0
    while row<m-1:
        check = matrix[row][0]
        if check == 0:
            row+=1
        else:
            break
    first_pivot = matrix[row]
    if first_pivot[0] == 0:
        print(None)
        matrix2 = matrix
    else:
        print(first_pivot)
        matrix2 = np.delete(matrix,row)

    check2 = 0
    row2 = 0
    while row2<len(matrix2)-1:
        check2 = matrix2[row2][1]
        if check2 == 0:
            row2+=1
        else:
            break
    second_pivot = matrix[row2]
    if second_pivot[1] == 0:
        print(None)
        matrix3 = matrix2
    else:
        print(second_pivot)
        matrix3 = np.delete(matrix2,row2)


def main2():
    col = 0
    smatrix = matrix
    m = len(smatrix)
    pivots = []

    pivot_col = 0
    while col<m:
        um = len(smatrix)
        check = 0
        row = 0
        while row<um-1:
            check = smatrix[row][col]
            if check == 0:
                row+=1
            else:
                break
        pivot = smatrix[row]
        
        if pivot[col] ==0:
            print(None)
            pivots.append(None)
        else:
            print(pivot)
            pivots.append(pivot)
            smatrix = np.delete(smatrix,row)
        col+=1

main2()

#print(np.array(matrix))
 

#Which row we are in the matrix
 #the columns number i.e horizontal placement in the row

#Check if [0] in row [0] is non zero. If it isn't zero, switch it to posisition row [0]
#Check if [0] in row [1] is non zero. If it isn't zero, switch with row [0]
