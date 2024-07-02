def solution(n, control):
    
    for i in range(len(control)):
        if control[i] == "w":
            n += 1
        elif control[i] == "s":
            n += -1
        elif control[i] == "d":
            n += 10
        elif control[i] == "a":
            n += -10

    return n


# 키-밸류 dic 으로 문제를 풀 수도 있다.

# def solution(n, control):
#     answer = n
#     c = { 'w':1, 's':-1, 'd':10, 'a':-10}
#     for i in control:
#         answer += c[i]
#     return answer