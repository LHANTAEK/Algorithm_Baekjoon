def solution(n):
    answer = []
    for i in range(n):
        result = [0] * n
        result[i] = 1
        answer.append(result)
    return answer
