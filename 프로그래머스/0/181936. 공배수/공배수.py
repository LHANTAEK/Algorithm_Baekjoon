def solution(number, n, m):
    answer = 0
    if (number % n == 0) & (number % m == 0):
        answer = 1
    else:
        answer = 0
    return answer
    

# 이렇게도 할 수 있음
# def solution(number, n, m):
#    answer = 0
#    return 1 if (number % n) == 0 & (number % m) == 0 else 0
