
import random
import string

ships = {"Carrier": 5, "Battleship":4,"Submarine": 3, "Destroyer": 2} 

bokstav = list(string.ascii_uppercase)


#Supplementary functions to help build our code
def column(table,j): 
    jthcolm = []
    for i in range(len(table)):
        row = table[i]
        jthcolm.append(row[j])
    return jthcolm

def display(table):
    y_d = bokstav[0:len(table)]
    x_d = list(range(1,len(table)+1))
    print(' ', *x_d)    
    for i in range(len(table)):
        strrow = y_d[i] + '|' + '|'.join(table[i]) + '|'
        print(strrow)

#Our code will revolve around this class which interacts with the 3 boards we will display namely board,playerboard, cheatboard. 
class TheSea:
    def __init__(self, width=10, height=10):
        self.width = width
        self.height = height
        self.bokstavset = bokstav[0:self.height]
        self.board = [[" "] * width for x in range(height)]
        self.playerboard = [[" "] * width for x in range(height)]
        self.cheatboard = [[" "] * width for x in range(height)]


    #This function will go through each coordinate in self.board and check the adjacent squares for sufficient empty space and edits the self.board so that we can apply other methods 
    def Place_Ship(self,ship): #We shall call this function with a different input every time for "Ship" 
        safe_list = [] 
        L = int(ships.get(ship))
        board = self.board
        for y in range(self.height):
            for x in range(self.width):
                try:
                    if y==0 and x==0:
                        if board[y][x:x+L+1] == [' ']*[L+1]:
                            safe_list.append([x,y,"Horizontal"])

                        if column(board,x)[y:y+L+1] == [' ']*(L+1) and column(board,x+1)[y:y+L] == ['W']*L:
                            safe_list.append([x,y,"Vertical"])

                    elif y==self.height-1 and x ==0:
                        if board[y][x:x+L+1] == [' ']*(L+1) and board[y-1][x:x+L] == ['W']*L:
                            safe_list.append([x,y,"Horizontal"])
                        
                    
                    elif x == 0 :
                        if board[y][x:x+L+1] == [' ']*(L+1) and board[y-1][x:x+L] == ['W']*L and board[y+1][x:x+L]== ['W']*L:
                            safe_list.append([x,y,"Horizontal"])

                        if column(board,x)[y-1:y+L+1] == [' ']*(L+2) and column(board,x+1)[y:y+L] == [' ']*L:
                            safe_list.append([x,y,"Vertical"])

                    elif y==0:
                        if board[y][x-1:x+L+1] == [' ']*(L+2) and board[y+1][x:x+L] == [' ']*L:
                            safe_list.append([x,y,"Horizontal"])
                        
                        if column(board,x)[y:y+L+1] == [' ']*(L+1) and column(board,x+1)[y:y+L] == [' ']*L and column(board, x-1)[y:y+L] == [' ']*L:
                            safe_list.append([x,y,"Vertical"])

                    else:
                        if board[y][x-1:x+L+1] == [' ']*(L+2) and board[y+1][x:x+L] == [' ']*L and board[y-1][x:x+L] ==[' ']*L:
                            safe_list.append([x,y,"Horizontal"])
                        
                        if column(board,x)[y-1:y+L+1] == [' ']*(L+2) and column(board,x+1)[y:y+L] == [' ']*L and column(board, x-1)[y:y+L] == [' ']*L:
                            safe_list.append([x,y,"Vertical"])
                        
                except:
                    pass

        val = random.choice(safe_list)
        x_r = val[0]
        y_r = val[1]

        if val[2] == "Horizontal": 
            self.board[y_r][x_r:x_r+L] = ['S']*L


        elif val[2] == "Vertical":
            for i in range(L):
                self.board[y_r+i][x_r] = "S"



        

    #This edits the self.playerboard and displays it based on your inputs and prints out a map of what youve missed and hit 
    def beskjuta(self):

        statement = False
        while statement == False: #This while statement will stop when the coordinates are unique i.e no "T" or "X" exist in those coordinates
            yb = ''
            xb = ''
            
            while yb not in self.bokstavset:
                yb = input("Ange y koordinat (bokstav mellan A-J): ").upper()
                if yb not in self.bokstavset:
                    print("Det där ligger utanför vår radar. Försök igen.",'\n')


            while xb not in list(range(1,self.width+1)) :
                xb = int(input("Ange x koordinat (ett integer mellan 1-10) "))
                if list(range(1,self.width+1)).count(xb)==0:
                    print("Det där ligger utanför vår radar. Försök igen.","\n")

            y = self.bokstavset.index(yb)
            x = int(xb) - 1 
            if self.playerboard[y][x] == "X" or self.playerboard[y][x] == "T":
                print("Du har redan provat den koordinaten. Försök igen.")

            elif self.playerboard[y][x] != "X" and self.playerboard[y][x] != "T" :
                statement = True

        if self.board[y][x] == "S":
            self.playerboard[y][x] = "T"
            print("Ett skepp har tagit emot träff")
        elif self.board[y][x] == " ":
            self.playerboard[y][x] = "X"
            print("Du har missat")


        display(self.playerboard) 

    def Ship_Count(self): #This will count how many "S" elemennts are left after shooting and return that count
        self.count = 0
        for x in self.board:
            self.count+=x.count("S")
        for x in self.playerboard:
            self.count-=x.count("T")

        return self.count 

    def score(self, turn_numb): #Each time the while loop in  main is run, we'll feed in the turn number and use it to get the träffprecentage 
        initial_count = 0
        for x in ships:
            initial_count+=int(ships.get(x))    
        träff = int(initial_count - self.count)

        return 'Traffprocent: ' + str((träff/turn_numb)*100) + ' %'

    def fuska(self): #Basically it displays  the ship posisitons of self.board and hits/misses in self.playerboard and prints them in display() format
        for y in range(self.height):
            for x in range(self.width):
                if self.board[x][y] == "S" and self.playerboard[x][y] != "T":
                    self.cheatboard[x][y] = "S"
                elif self.playerboard[x][y] == "T":
                    self.cheatboard[x][y] = "T"
                elif self.playerboard[x][y] == "X":
                    self.cheatboard[x][y] = "X"      
        
        display(self.cheatboard)







def main(): #This will run the methods above depending on how you interact with the huvudmenyn
    game = TheSea()
    for x in ships:
        game.Place_Ship(x)
    turn_numb = 1
    while game.Ship_Count()>0: #This will continue running until no ships are left
        print('\n','Dina val möjligheter (1-3):', '\n', '1) Beskjuta fiendefartyg','\n' ,'2) Fuska','\n' , '3) Avsluta','\n')
        try:
            svar = int(input('Ditt val: '))
            print()
            if svar == 1:
                game.beskjuta()
                game.Ship_Count()
                print(game.score(turn_numb), '\n', "Tur#: "+str(turn_numb),'\n')
                turn_numb+=1
            elif svar == 2:
                game.fuska()
            elif svar == 3:
                game.fuska()
                break
        except:
            print("Ogiltig svar. Försök igen.")
    if game.Ship_Count()==0:
        print("Inga skepp finns kvar. Du vann.")



main()