ideaList = [] 
idea_store = []
import time

def read_text(file_name):
 with open(file_name,'r') as adatok:
    line = adatok.readlines()
    idea_store.append(line)
    print(idea_store)

while True:
 ideainput = input("Add meg az ötleted: ")
 clearidea = ideainput.strip() 
 print(clearidea)
 idea_store.append(clearidea)
  
 with open('sorok.txt', 'a') as filehandle:  

  for idea in idea_store:
    filehandle.writelines(idea_store)
    #filehandle.writelines("%s\n" % idea)

   #("%s\n" % idea for idea in ideaList), ("\n"+str(ideaList)+"\n")

  read_text('sorok.txt')