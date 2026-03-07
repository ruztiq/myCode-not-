import Taschenrechner_art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {"+": add, "-": subtract, "*": multiply, "/":divide,}

def taschenrechner():
    print(Taschenrechner_art.logo)
    weiter_rechnen = True
    n1 = int(input("Geben Sie erste Zahl ein: "))
    while weiter_rechnen:
        print(art.logo)
        for symbol in operations:
            print(symbol)
        operator = input("Gebene Sie den Operator ein: ")
        n2 = int(input("Geben Sie zweite Zahl ein: "))
        answer = operations[operator](n1, n2)
        print(f'{n1} {operator} {n2} = {answer}')

        choise = input(f'Wollen Sie mit der Zahl {answer} weiter rechnen? y or n ')
        if choise == "y":
            n1 = answer
        else:
            weiter_rechnen = False
            print("\n" * 20)
            taschenrechner()

taschenrechner()




