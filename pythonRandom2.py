attacker = []
defender = []

import random

def attack(number_of_dice):
    if number_of_dice >=4:
        print("A szám érvénytelen")
        exit()
    for i in range(number_of_dice):
        attacker.append(random.randint(1,6))


def defend(n):
    if n>=3:
        print("A szám érvénytelen")
        exit()    
    x = 1
    while x<=n:
        defender.append(random.randint(1,6))
        x = x+1

attack(int(input("Add meg a támadok számát: ")))
tamado = sorted(attacker, reverse=True)

defend(int(input("Add meg a védök számát: ")))
vedo= sorted(defender, reverse=True)

print(tamado)
print(vedo)

if tamado[0]>vedo[0]:
    print("Vedő elvesztette az 1. egységet")
else: 
    print("1. támadás sikertelen")

if tamado[1]>vedo[1]:
    print("Vedő elvesztette a  2. egységet")
else:
    print("2. támadás sikertelen")

if tamado[0]>vedo[0] and tamado[1]>vedo[1]:
    print("A vedő vesztesége: -2")
elif tamado[0]>vedo[0] and tamado[1]<=vedo[1]:
    print(" A védő vesztesége  : -1 \n A támado vesztesége: -1")
elif tamado[0]<=vedo[0] and tamado[1]>vedo[1]:
    print(" A védő vesztesége  : -1 \n A támado vesztesége: -1")  
else:
    print("A támadó vesztesége: -2")