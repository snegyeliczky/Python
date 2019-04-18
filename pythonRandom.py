attacker = []
defender = []

import random
for kocka in range(1):
 attacker.append(random.randint(1,6))
 attacker.append(random.randint(1,6))
 attacker.append(random.randint(1,6))
 tamado = sorted(attacker, reverse=True)
 defender.append(random.randint(1,6))
 defender.append(random.randint(1,6))
 vedo = sorted(defender, reverse=True)

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