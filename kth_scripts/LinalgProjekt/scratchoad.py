# from sympy import *
# import turtle
# from tkinter import *
# import random
# import numpy as np



# '''
# w = Tk()
# w.configure(background = "light blue")
# w.title('Blah')
# w.geometry('270x150-1000+500')

# global x     
# x=0
# def click():
#     global x
#     x+=1
#     print(x)

# bl = Button(w, text='blah', command=click)

# bl.pack()


# w.mainloop()




# #Notes
# #Each color ranges from 0 to 255 bc of geo series
# '''


# '''
# xsize = 6
# ysize = 8
# bräde = [[0]*ysize]*xsize
# for i in range(xsize):
#     for j in range(ysize):
#         print(bräde[i][j], end = '<')
#     print()
# '''
# '''class pwn:
#     def __init__(self,färg):
#         self.färg = färg
#         self.pos=0

#     def move(self, step):
#         self.pos = self.pos+step

# p1 = pwn('Röd')

# class board:
#     def __init__(self, name):
#         self.name = name
#         self.pawns = list()

#     def addpawn(self,p):
#         return self.pawns.append(p)
    
# b1 = board('Blah')

# b1.addpawn(pwn('Blah1'))
# b1.addpawn(pwn('blah3'))'''

# '''from math import *

# blah = [['w','w','w','w'],['w','w','w','w'],['s','w','w','w']]

# safe_list = []


# for i, j in enumerate(blah):
#     if j == ['w','w','w']:
#         safe_list.append(i)

# '''



# # -------------Setting the board, players and hiding battleships-------------
# '''
# board = []

# for x in range(0,5):
#   board.append(["o"] * 5)

# def print_board(board):
#   for row in board:
#     print (" ".join(row))

# print("Let's play Battleship!")
# print("This is a 2 player game")

# player_1 = input("Enter first name: ")
# player_2 = input("Enter second name: ")
# players = [player_1, player_2]

# def random_player(players):
#     return random.choice(players)

# def random_row(board):
#   return random.randint(0,len(board)-1)

# def random_col(board):
#   return random.randint(0,len(board[0])-1)

# if random_player(players) == player_1:
#   print(player_1, "starts the game.")
# else:
#   print(player_2, "starts the game.")
  
# ship_row_1 = random_row(board)
# ship_col_1 = random_col(board)
# # print (ship_row_1)
# # print (ship_col_1)

# ship_row_2 = random_row(board)
# ship_col_2 = random_col(board)
# # print (ship_row_2)
# # print (ship_col_2)

# print_board(board)

# player_start = random_player(players)
# # ----------------------------Playing the game----------------------------



# hit_count = 0

# for turn in range(4):
#      guess_row = int(input("Guess Row: (allowed values: 0-4) "))
#      guess_col = int(input("Guess Col: (allowed values: 0-4) "))

#      if (guess_row == ship_row_1 and guess_col == ship_col_1) or (guess_row == ship_row_2 and guess_col == ship_col_2):
#             hit_count = hit_count + 1
#             board[guess_row][guess_col] = "*"
#             print ("Congratulations! ")
#             if hit_count == 1:
#                    print("You sunk first battleship!") 
#             elif hit_count == 2:
#                    print("You sunk second battleship! You win!")
#                    print_board(board)
#                    break
#      else:
#             if (guess_row < 0 or guess_row > 4)  or (guess_col < 0 or guess_col > 4):
#                    print ("Oops, that's not even in the ocean.")
#             elif(board[guess_row][guess_col] == "X"):
#                    print ("You guessed that one already.")
#             else:
#                  print ("You missed my battleship!")
#                  board[guess_row][guess_col] = "X"
#             print (turn + 1, "turn")
#      print_board(board)
# print ("Ship 1 is hidden:")    
# print (ship_row_1)
# print (ship_col_1)

# print ("Ship 2 is hidden:")    
# print (ship_row_2)
# print (ship_col_2)'''


# def matrix(n):
#   matrix = [[0]*n for x in range(n)]
#   for i in range(n):
#     if i == 0:
#       matrix[0][0:2] = [1,1]
#     elif i == n-1:
#       matrix[n-1][n-2:n] = [1,1]
#     else:
#       matrix[i][i-1:i+2] = [1,1,1]
#   return matrix



# def main1():
  
#   for i in range(3,12):
#     M = Matrix(matrix(i))
#     mr = M.rref()
#     if mr[i-1][i-1] == 0:
#       print(i)

# def main2():
#   for i in range(2,30):
#     M = Matrix(matrix(i))
#     mr = det(M)
#     print(mr, i)

# def main3():
#   s = [1,2,3]
#   x=False
#   round = 1
#   p1p = 0
#   p2p = 0
#   while round<5:
#     while x==False:
#       print("Round: ", round)
#       print(" 1:Rock \n 2:Paper \n 3:Scissors")
#       p1 = input("p1 Please enter one option ")
#       p2 = input("p2 Please enter one option ")
#       try:
#         p1 = int(p1)
#         p2 = int(p2)
#         if s.count(int(p1))==0 or s.count(int(p2))==0:
#           print("Try again\n")
#         elif s.count(int(p1)) == 1 or s.count(int(p2)) == 1:
#           x=True
#       except:
#         x=False
#         print("Bad input")
#     if p1 == p2:
#       print("Tie")
#     elif p1 == 1 and p2 == 2: #Rock v paper
#       p2p +=1
#       print("Win for p2")
#     elif p1 == 2 and p2 == 1:  # Paper v rock
#       print("Win for p1")
#       p1p += 1
#     elif p1 == 1 and p2 == 3: #rock v scissors
#       p1p +=1
#       print("win for p1")
#     elif p1 == 3 and p2 == 1: #scissors v rock
#       p2p +=1
#       print("Win for p2")
#     elif p1 == 2 and p2 ==3: #paper v scissors
#       print("win for p2")
#       p2p+=1
#     elif p1 == 3 and p2 == 2: #Scissors v paper
#       print("Win for p2")
#       p2p+=1

#     round+=1

# def make_transmatrix(ord_list):
#     unika_ord = []
#     for ord in ord_list:
#       if ord not in unika_ord:
#         unika_ord.append(ord)
  
#     dim = len(unika_ord)
#     Övergångs_matris = [[0.0]*dim for x in range(dim)]
#     for i in range(len(ord_list)-1):
#       undex1 = unika_ord.index(ord_list[i])
#       undex2 = unika_ord.index(ord_list[i+1])
#       Övergångs_matris[undex1][undex2] += float(1.0)
#       Övergångs_matris = np.array(Övergångs_matris)
#       for row in range(Övergångs_matris.shape[0]):
#         rowsum = np.sum(Övergångs_matris[row])
#         if rowsum > 0:
#           Övergångs_matris[row] /= rowsum
#     return Övergångs_matris


# def main4(txt):
#   text_file = open(txt, 'r', encoding='utf-8')
#   text = text_file.read()
#   words = text.split()
#   print(words)
#   with open(txt,'w',encoding='utf-8') as x:
#     for line in words:
#       x.write(line)
#       x.write('\n')
#       x.write('\n')


# def list(txt):
#     text_file = open(txt,'r', encoding='utf-8')
#     text = text_file.read()
#     words = text.split()
#     uniquel = []
#     for word in words:
#       if word not in uniquel:
#         uniquel.append(word)
#     return uniquel

# # list4 = list('kanjin4.txt')
# # list3 = list('kanshudon2.txt')
# # list2 = list('kanjina.txt')
# # list1 = list('kanshudon3.txt')


# # s=[]
# # s2=[]
# # s3=[]
# # for x in list1: #kanji only in kenshudo
# #   if x not in list2:
# #     s.append(x)
# # for x in list2: #kanji only in kanjistudy
# #   if x not in list1:
# #     s2.append(x)


# class particle():
#   def __init__(self,x=0,y=0,z=0):
#     self.x = x;
#     self.y = y;
#     self.z = z;
#   def go_up(self):
#     self.z+=1
# box1 = particle(2, 3)
# box2 = particle(3, 1, 4)
# def main():
#   box1.z = 2
#   for i in range(3):
#     box1.go_up()
#   print(box1.x,box1.y,box1.z)

# class blah(particle):
#   pass

# x = lambda a : a + 10;

# text_file = open('kanshudon3.txt', 'r', encoding='utf-8')
# text = text_file.read()
# i=0
# r=0
# for t in text:
# 	if t == '\n':
# 		r+=1
# 	if t == '	':
# 		i+=1
# 	if i == 159 or r==693:
# 		break
file = open('tst2.txt','r',encoding='utf-8').read().split('\n\n')

new_list = []

for i in range(len(file)):
	if i%2==0:
		new_list.append(file[i])
		# print(file[i])


pop = open('txtpop.txt','w',encoding='utf-8')
for x in new_list:
	pop.write(x)
	pop.write('\n\n')