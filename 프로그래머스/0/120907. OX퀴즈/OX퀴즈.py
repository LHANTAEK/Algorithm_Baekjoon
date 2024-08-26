def solution(quiz):
    result = []
    for equation in quiz:
        left, right = equation.split('=')
        x, op, y = left.strip().split()
        
        x = int(x)
        y = int(y)
        z = int(right.strip())
        
        if op == '+':
            calculated = x + y
        elif op == '-':
            calculated = x - y
        
        if calculated == z:
            result.append("O")
        else:
            result.append("X")
    
    return result