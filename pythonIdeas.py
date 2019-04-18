
ideaList = [] 
import time

def read_text(file_name):
 with open(file_name,'r') as adatok:
    while True:
      line = adatok.readline()
      if line:
        print(line.strip())
        time.sleep(0.5) 
      else:
        break
    adatok.close()

while True:
 ideainput = input("Add meg az ötleted: ")
 clearidea = ideainput.strip() 
 print(clearidea)
 ideaList.append(clearidea)
  
 with open('sorok.txt', 'a') as filehandle:  

  for idea in ideaList:
    filehandle.writelines(idea + "\n")
    #filehandle.writelines("%s\n" % idea)

   #("%s\n" % idea for idea in ideaList), ("\n"+str(ideaList)+"\n")


  read_text('sorok.txt')