def calculator(num1,operator,num2):
    if operator == "+":
        eredmeny = num1+num2
        return eredmeny
    elif operator == "-":
        eredmeny = num1-num2
        return eredmeny
    elif operator == "*":
        eredmeny = num1*num2
        return eredmeny
    elif operator == "÷":
        eredmeny = num1/num2
        return eredmeny

def main():
    num1 = float(input("add meg az elsö számot: "))
    operator = input("add meg az operátor: ")
    num2 = float(input("add meg a másik számot: "))

    print(calculator(num1,operator,num2))

main()