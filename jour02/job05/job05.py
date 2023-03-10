

def calcule(num1, operator, num2):

    num1 = int(input("enter 1st number : "))
    num2 = int(input("enter 2nd number : "))

    import random
    op_list = ["+", "-", "*", "/", "%"]
    operator = random.choice(op_list)
    print (operator)

    if operator == "+":
        print (num1 + num2)
    elif operator == "-":
        print (num1 - num2)
    elif operator == "*":
        print (num1 * num2)
    elif operator == "%":
        print (num1 % num2)


calcule (0, 0, 0)

