def solution(arr):
    answer = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] != arr[j][i]:
                answer = 0
                return answer
            else:
                answer = 1
    return answer


# 다른 풀이

def solution(arr):
    return int(arr == list(map(list, zip(*arr))))
