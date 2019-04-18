def gramer_maker(word):
    if word[-2:] == "ie": 
        original = word
        word = word.replace(word[-2:],"ying")
        print(original+" --- "+word)
    if word[-1]=="e":
        original = word
        word = word.replace(word[-1],"ing")
        print(original+" --- "+word)
    else:
        original = word
        word = word+"ing"
        print(original+" --- "+word)


gramer_maker(input("Add meg az igéd: "))

