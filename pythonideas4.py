def file_reader (file_name):
    with open(file_name,"r") as file_for_read:
        file_container = []
        for lines in file_for_read:     #lines = file_for_read.readline()
                lines_for_clean = (str(len(file_container)+1)+": "+lines)
                print(lines_for_clean)
                clean_lines = lines_for_clean.strip() 
                file_container.append(clean_lines)
        file_container.clear()  
        
def file_appender(file_name):
    with open (file_name,"a") as file_for_write:
        idea_input = input("Add meg az ötleted: ")
        clean_idea = idea_input.strip()
        file_for_write.writelines(clean_idea+"\n")
        #file_container.append(clean_idea)
        #print(file_container)

def delet_line(file_name,line_to_del):
    with open(file_name,"r") as f:
        lines = f.readlines()
    with open(file_name,"w") as f:
        for i in range(len(lines)):
            if i != line_to_del:
                f.write(lines[i])

def selector(select):
        if select == 1:
            file_appender("sorok.txt")
        elif select == 2:
            file_reader("sorok.txt")
        elif select == 3:
            delet_line("sorok.txt",int(input("Add meg hanyadik sor töröljem: "))-1)
        elif select == 4:
            exit()
        else:
            print("1: uj ötlet megadás\n"+"2: ötletek beolvasása\n"+"3: ötlet törlése\n"+"4: exit\n")
            selector(int(input("Add meg mit akarsz: ")))


while True:
    print("1: uj ötlet megadás\n"+"2: ötletek beolvasása\n"+"3: ötlet törlése\n"+"4: exit\n")
    selector(int(input("Add meg mit akarsz: ")))