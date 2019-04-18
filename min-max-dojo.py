numbers = [-5, 23, 0, -9, 12, 99, 105, -43]

def maximum(szamok):
    max_number = szamok[0]
    for number_in_numbers in szamok: 
        if max_number < number_in_numbers:
            max_number = number_in_numbers
    return max_number


def minimum(szamok):
    max_number = szamok[0]
    for number_in_numbers in szamok: 
        if max_number > number_in_numbers:
            max_number = number_in_numbers
    return max_number


def averige(szamok):
    averige_number = 0
    for lista_index in range(len(szamok)):
        averige_number += szamok[lista_index]
    print(averige_number)
    #averige_number=averige_number/len(szamok)
    return averige_number/len(szamok)



print(maximum(numbers))
print(minimum(numbers))
print(averige(numbers))






'''
for i in range(len(numbers)):
    if numbers[i]>=numbers[i+1]:
        number_to_switch = numbers[i+1]
        numbers[i+1] = numbers[i]
        numbers[i] = number_to_switch
print(numbers)
'''


