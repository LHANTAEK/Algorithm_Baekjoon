def solution(arr, queries):
    answer = []
    for s, e, k in queries:
        min_value = -1
        for i in range(s, e + 1):
            if arr[i] > k:
                if min_value == -1 or arr[i] < min_value:
                    min_value = arr[i]
        answer.append(min_value)
    return answer
