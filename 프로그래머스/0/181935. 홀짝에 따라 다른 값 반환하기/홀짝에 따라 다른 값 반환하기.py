def solution(n):
    answer = 0
    if n % 2 == 1:
        for i in range(0,n+1):
            if i % 2 == 1:
                answer += i        
    else:
        for i in range(0, n+1):
            if i % 2 == 0:
                answer += i**2
    return answer

# 이렇게 풀 수도 있다.
# def solution(n):
#     if n % 2 == 1:
#         return sum(range(1, n+1, 2))
#     return sum([i*i for i in range(2, n+1, 2)])