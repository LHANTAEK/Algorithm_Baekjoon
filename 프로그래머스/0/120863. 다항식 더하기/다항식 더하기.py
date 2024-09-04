def solution(polynomial):
    x_coef = 0
    constant = 0
    
    for i in polynomial.split(' + '):
        if 'x' in i:
            if i == 'x':
                x_coef += 1
            else:
                x_coef += int(i[:-1])
        else:
            constant += int(i)
    
    if x_coef == 0:
        answer = f"{constant}"
        return answer
    
    elif constant == 0:
        if x_coef == 1:
            answer = f"x"
        else: 
            answer = f"{x_coef}x"
        return answer
    
    else:
        if x_coef != 1:
            answer = f"{x_coef}x + {constant}"
        else:
            answer = f"x + {constant}"
        return answer