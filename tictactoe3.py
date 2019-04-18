import os
import time
import random

board = [" "," "," "," "," "," "," "," "," "," ",]

def print_board():
    print(" "+board[1]+"  | "+board[2]+" |  "+board[3]+"  ")
    print("----|---|----")
    print(" "+board[4]+"  | "+board[5]+" |  "+board[6]+"  ")
    print("----|---|----")
    print(" "+board[7]+"  | "+board[8]+" |  "+board[9]+"  ")

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



while True:
    os.system("clear")
    print_board()

    choice = int(input("Please choose an empty space for X: "))
    if board[choice] == " ":
        board[choice] = "X"
        os.system("clear")
        print_board()
        game_over(board)
        
    choice = int(input("Please choose an empty space for O: "))
    if board[choice] == " ":
        board[choice] = "O"
        os.system("clear")
        print_board()
        game_over(board)
        
    else:
        print("Sorry that is no good")
        time.sleep(1)
    
    
