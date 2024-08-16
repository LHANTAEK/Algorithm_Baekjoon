def solution(hp):
    answer = 0
    a = hp // 5 # 4
    a_rest = hp % 5 # 4
    b = a_rest // 3 # 1
    c = a_rest % 3 
    
    answer = a + b + c
    return answer