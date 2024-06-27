def solution(a, b):
    answer = 0
    if a < b:
        if str(a) + str(b) < str(b) + str(a):
            answer = int(str(b) + str(a))
        else:
            answer = int(str(a) + str(b))
            
    else:
        if str(a) + str(b) < str(b) + str(a):
            answer = int(str(b) + str(a))
        else:
            answer = int(str(a) + str(b))
                  
    return answer