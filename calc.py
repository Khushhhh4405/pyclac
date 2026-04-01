# Perform simple arithmetic encoded in an input string:
# '1 + 2' -> 3, or '1 - 2' -> -1.
def compute(expression):
    values = expression.split(' ')
    num0 = int(values[0])
    operator = values[1]
    num1 = int(values[2])
    if operator == '+':
        return num0 + num1
    else:
        print('unknown operator!')
        return 0
    
def compute(expression):
    values = expression.split(' ')
    num0 = int(values[0])
    operator = values[1]
    num1 = int(values[2])
    if operator == '+':
        return num0 + num1
    elif operator == '-':
        return num0 - num1
    else:
        print('unknown operator!')
        return None
    
def compute(expression):
    num0, operator, num1 = expression.split(' ')
    if operator == '+':
        return num0 + num1
    elif operator == '-':
        return num0 - num1
    else:
        print('unknown operator!')
        return None