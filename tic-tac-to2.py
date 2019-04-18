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

def control():
    for i in range(len(board)):
        if board[i]== "X" and board[i+1] == "X" and board[i+2] == "X":
            print("X winn")
            

while True:
    os.system("clear")
    print_board()

    choice = int(input("Please choose an empty space for X: "))
    if board[choice] == " ":
        board[choice] = "X"
        os.system("clear")
        print_board()
        control()
        
    choice = int(input("Please choose an empty space for O: "))
    if board[choice] == " ":
        board[choice] = "O"
        os.system("clear")
        print_board()
        
    else:
        print("Sorry that is no good")
        time.sleep(1)
    
