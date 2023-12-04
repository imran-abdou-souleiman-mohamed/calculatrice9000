def evaluer_expression(a, op, b):
    if op == '*':
        return a * b
    elif op == '/':
        if b == 0:
            raise ZeroDivisionError("Division par zéro n'est pas autorisée.")
        return a / b
    elif op == '+':
        return a + b
    elif op == '-':
        return a - b

def calculer(expression):

    expression = expression.strip()
    elements = expression.split(" ")

    valid = set(['*', '/', '+', '-'])
    for element in elements:
        if not element.isdigit() and element not in valid:
            print("Erreur: Expression invalide")
            return

    
    stack = []

    i = 0
    while i < len(elements):
     

        if elements[i] in ['*', '/', '+', '-']:
            stack.append(elements[i])
        else:
            if len(stack) > 0 and stack[-1] in ['*', '/']:
                op = stack.pop()
                a = int(stack.pop())
                result = evaluer_expression(a, op, int(elements[i]))
                stack.append(result)
            else:
                stack.append(elements[i])  
        i += 1


    result = 0
    while len(stack) > 1:
        b = int(stack.pop())
        op = stack.pop()
        a = int(stack.pop()) if stack else 0
        result = evaluer_expression(a, op, b)
        stack.append(result)

    print("Résultat :", stack[0])

expression = input("Veuillez rentrer votre calcule : \nOpérateurs permis * / + - : ")
# exemple : expression = "24 + 4 * 3 - 6 / 2 * 5"
calculer(expression)