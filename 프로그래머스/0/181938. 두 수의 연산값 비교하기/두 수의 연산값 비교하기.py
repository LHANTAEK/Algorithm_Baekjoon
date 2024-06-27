def solution(a, b):
    answer = 0
    if int(str(a)+str(b)) >= 2 * a * b:
        answer = int(str(a) + str(b))
    else:
        answer = 2 * a * b
    return answer

# max 모듈을 쓰면 쉽다!

# def solution(a,b):
#     return max(int(str(a) + str(b)), 2 * a * b)