import time
import os

letter_list = []

def word_to_finde (word):
    listed_word = list(word)
    for i in range(len(listed_word)):
        letter_list.append("_")
    return listed_word


def lives (betu,betulista):
    global life
    if betu not in betulista:
        life=life-1
        print("\nYou have "+str(life)+" life left!")
        hanger (life)
    
    if life == 0:
        print("You dont have more possibility... You Died!!!\nThe word was: ", end='')
        for i in listed_word_to_finde:
            print(i, end='')
        print("")
        exit()


def Asking_letters(letter):
    lives(letter,listed_word_to_finde)          #life check
    if letter in letter_list:                   # duplication control
        print("This letter has allready given")
        time.sleep(1)
    elif letter in listed_word_to_finde:        #letter adder
        x = 0
        for i in listed_word_to_finde:
            if letter == i:
                letter_list[x] = i
            x += 1

def game_over (list1,list2):
    if list1 == list2:
        print("You won the game... We don't hang you today... :(")
        exit()

def hanger (life):

    if life == 4:
        print("\n__ __") 
    if life == 3:
        print("\n__|__")
    if life == 2:
        print("\n  |  ")
        print("__|__")     
    if life == 1:
        print("\n   ____")
        print("  |  ")
        print("__|__")  
    if life == 0:
        print("\n   ____")
        print("  |   DIE")
        print("__|__")    

#main

listed_word_to_finde = word_to_finde(input("Give me the hanger word!!  "))
life=len(letter_list)

while True:
    os.system("clear")
    hanger (life)
    print("\n")
    for i in letter_list:
        print(i +"  ", end='')
    Asking_letters(input("Give me a letter: "))
    game_over(listed_word_to_finde,letter_list)
    

