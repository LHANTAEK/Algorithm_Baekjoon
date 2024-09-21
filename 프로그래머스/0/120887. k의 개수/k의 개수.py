def solution(i, j, k):
    answer = 0
    for p in range(i,j+1):
        for q in list(str(p)):
            if str(k) == q:
                answer += 1
            
    return answer