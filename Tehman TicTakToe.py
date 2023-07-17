import random

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]
currentplayer = "T"
winner = None
gamerunning = True




#first making game board
def printBoard(board):
    print(board[0] +" | " + board[1] +" | " + board[2])
    print('---------')
    print(board[3] +" | " + board[4] +" | " + board[5])
    print('---------')
    print(board[6] +" | " + board[7] +" | " + board[8])



#player input take
def playerinput(board):
    inp = int(input("Enter a number from 1-9: "))
    if inp >= 1 and inp <=9 and board[inp-1] =="-":
        board[inp-1] = currentplayer
    else:
        print("You have selected wrong spot")



#checking for win tie
def checkhorizontal(board):
    global winner
    if board[0]==board[1]==board[2] and board[1] !="-":
        winner = board[0]
        return True
    elif board[3]==board[4]==board[5] and board[3]!="-":
        winner = board[3]
        return True
    elif board[6]==board[7]==board[8] and board[6]!="-":
        winner = board[6]
        return True
    

def checkRow(board):
    global winner
    if board[0]==board[3]==board[6] and board[0] !="-":
       winner = board[0]
       return True
    elif board[1]==board[4]==board[7] and board[1] !="-":
        winner = board[1]
    elif board[2]==board[5]==board[8] and board[2] !="-":
        winner = board[2]
        return True
    
def checkDiag(board):
    global winner
    if board[0]==board[4]==board[8] and board[0] !="-":
        winner = board[0]
        return True
    elif board[2]==board[4]==board[6] and board[2] !="-":
        winner = board[2]
        return True
    
def checkTie(board):
    if "-" not in board:
        printBoard(board)
        print("HAHAHA It was a tie")
        gamerunning = False

def checkWin():
    if checkDiag(board) or checkhorizontal(board) or checkRow(board):
        print(f"Finally The winner is {winner} ")



def switchPlayer():
    global currentplayer
    if currentplayer == "T":
        currentplayer = "O"
    else:
        currentplayer = "T"


#AI
def computer(board):
    while currentplayer =="O":
        p = random.randint(0, 8)
        if board[p]=="-":
            board[p]="O"
            switchPlayer()





while gamerunning:
    printBoard(board)
    playerinput(board)
    checkWin()
    checkTie(board)
    switchPlayer()
    computer(board)
    checkWin()
    checkTie(board)

