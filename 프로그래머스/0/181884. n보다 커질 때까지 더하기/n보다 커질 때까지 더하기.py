def solution(numbers, n):
    answer = 0
    for i in range(len(numbers)):
        if sum(numbers[:i+1]) > n:
            answer = sum(numbers[:i+1])
            return answer