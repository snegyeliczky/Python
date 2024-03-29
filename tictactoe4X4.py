import os
import time
import random

board = [" "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," "," ",]

def print_board():
    print(" "+board[1]+"  | "+board[2]+"  |  "+board[3]+" |  "+board[4]+"  ")
    print("----|----|----|-----")
    print(" "+board[5]+"  | "+board[6]+"  |  "+board[7]+" |  "+board[8]+"  ")
    print("----|----|----|----")
    print(" "+board[9]+"  | "+board[10]+"  |  "+board[11]+" |  "+board[12]+"  ")
    print("----|----|----|----")
    print(" "+board[13]+"  | "+board[14]+"  |  "+board[15]+" |  "+board[16]+"  ")


def game_over(game_board):
    for i in range(1,8,3):
        if game_board[i] == "X" and game_board[i+1] == "X" and game_board[i+2] == "X":
            print("X won!")
            quit()
        if game_board[i] == "O" and game_board[i+1] == "O" and game_board[i+2] == "O":
            print("O won!")
            quit()
    for i in range(1,4):
        if game_board[i] == "X" and game_board[i+3] == "X" and game_board[i+6] == "X":
            print("X won!")
            quit()
        if game_board[i] == "O" and game_board[i+3] == "O" and game_board[i+6] == "O":
            print("O won!")
            quit()
    if game_board[1] == "X" and game_board[5] == "X" and game_board[9] == "X":
        print("X won!")
        quit()
    if game_board[3] == "X" and game_board[5] == "X" and game_board[7] == "X":
        print("X won!")
        quit()
    if game_board[1] == "O" and game_board[5] == "O" and game_board[9] == "O":
        print("O won!")
        quit()
    if game_board[3] == "O" and game_board[5] == "O" and game_board[7] == "O":
        print("O won!")
        quit()

    x = 0
    for i in range(1,17):
        if game_board[i] == " ":
             x+=1
    if x == 0:
        print("Draw!")
        quit()

def input_choiceX():
    try:
        position = int(input("Please choose an empty space for X: "))
        if position < 1 or position > 16:
            raise ValueError
        elif board[position] == " ":
            board[position] = "X"
        else:
            print("Sorry this place is reserved")
            time.sleep(1)
            raise ValueError
    except:
        print("Pleas give a valid position!")
        input_choiceX()

def input_choiceY():
    try:
        position = int(input("Please choose an empty space for O: "))
        if position < 1 or position > 16:
            raise ValueError
        elif board[position] == " ":
            board[position] = "O"
        else:
            print("Sorry this place is reserved")
            time.sleep(1)
            raise ValueError
    except:
        print("Pleas give a valid position!")
        input_choiceY()


while True:
    os.system("clear")
    print_board()

    input_choiceX()
    os.system("clear")
    print_board()
    game_over(board)
        
    input_choiceY()
    os.system("clear")
    print_board()
    game_over(board)
        
    
    
