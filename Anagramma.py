def file_reader(file_for_read,anagramma):
    listed_anagramma=list(anagramma)
    sorted_anagramma=sorted(listed_anagramma)
    #print(sorted_anagramma)
    with open(file_for_read) as readed_file:
        for line in readed_file:
            cleand_line=line.strip()
            listed_line= list(cleand_line)
            sorted_line=sorted(listed_line)
            #print(sorted_line)
            if sorted_line == sorted_anagramma:
                print(cleand_line+" és "+anagramma+" Anagramma!!")




def anagramas(word1,word2):
    word1_list=list(word1)
    word1_sorted= sorted(word1_list)
    print(word1_sorted)
    word2_list=list(word2)
    word2_sorted = sorted(word2_list)
    print(word2_sorted)
    if word2_sorted == word1_sorted:
        print("Anagramma")
    else:
        print("Nem anagramma")


anagramas(input("add meg az elsö szót: "),input("addmeg a második szót: "))
#file_reader("sorok.txt",input("Add meg mit hasonlítsak össze: "))