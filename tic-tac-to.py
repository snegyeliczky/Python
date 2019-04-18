game = [["0","0" ,"0" ],["0","0","0"],["0","0","0"]]
print("   0  1  2")
for count, row in enumerate(game):
        print(count, row)

def game_end():
    for i in range(3):
        if game[i][0] == "x" and game[i][1] == "x" and game[i][2] == "x":
            print("x win!")
            exit()
        if game[0][i] == "x" and game[1][i] == "x" and game[2][i] == "x":
            print("x win!")
            exit()
        if game[0][0] == "x" and game[1][1] == "x" and game[2][2] == "x":
            print("x win!")
            exit()
        if game[0][2] == "x" and game[1][1] == "x" and game[2][0] == "x":
            print("x win!")
            exit()

        if game[i][0] == "o" and game[i][1] == "o" and game[i][2] == "o":
            print("o win!")
            exit()
        if game[0][i] == "o" and game[1][i] == "o" and game[2][i] == "o":
            print("o win!")
            exit()
        if game[0][0] == "o" and game[1][1] == "o" and game[2][2] == "o":
            print("o win!")
            exit()
        if game[0][2] == "o" and game[1][1] == "o" and game[2][0] == "o":
            print("o win!")
            exit()


while True:
    game[int(input("add meg az y: "))][int(input("add meg az x: "))]="x"
    print("   0  1  2")
    for count, row in enumerate(game):
        print(count, row)
        game_end()
    print("player2")
    game[int(input("add meg az y: "))][int(input("add meg az x: "))]="o"
    print("   0  1  2")
    for count, row in enumerate(game):
        print(count, row)
        game_end()

