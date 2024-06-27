def solution(a, b):
    answer = 0
    if a < b:
        if int(str(a) + str(b)) < int(str(b) + str(a)):
            answer = int(str(b) + str(a))
        else:
            answer = int(str(a) + str(b))
            
    else:
        if int(str(a) + str(b)) < int(str(b) + str(a)):
            answer = int(str(b) + str(a))
        else:
            answer = int(str(a) + str(b))
                  
    return answer

# max(a,b)를 사용해서 풀 수도 있다!
# def solution(a,b):
#     return int(max(f"{a}{b}", f"{b}{a}"))