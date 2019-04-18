lista=[]
import time

adatok = open('sorok.txt','w')
for sor in adatok:
    clearsor = sor.strip()
    lista.append(clearsor)

print(lista)

adatok.close()

adatok=open('sorok.txt','r')
while True:
  i = adatok.readline()
  if i:
    print(i.strip())
    time.sleep(0.5)