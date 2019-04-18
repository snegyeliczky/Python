file_container = [] 

def file_reader (file_name):
    with open(file_name,"r") as file_for_read:
        for lines in file_for_read:     #lines = file_for_read.readline()
                lines_for_clean = (str(len(file_container)+1)+": "+lines)
                print(lines_for_clean)
                clean_lines = lines_for_clean.strip()
                file_container.append(clean_lines)  

        

def file_appender(file_name):
    with open (file_name,"a") as file_for_write:
        idea_input = input("Add meg az ötleted: ")
        clean_idea = idea_input.strip()
        file_for_write.writelines("\n"+ clean_idea)
        file_container.append(str(len(file_container)+1)+": "+clean_idea)
        #print(file_container)

file_reader("sorok.txt")
file_appender("sorok.txt")