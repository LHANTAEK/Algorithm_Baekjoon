def solution(arr, queries):
    answer = []
    for query in queries:
        s, e, k = query
        temp = []
        for x in arr[s:e+1]:
            if x > k:
                temp.append(x)
        answer.append(-1 if not temp else min(temp))
    return answer