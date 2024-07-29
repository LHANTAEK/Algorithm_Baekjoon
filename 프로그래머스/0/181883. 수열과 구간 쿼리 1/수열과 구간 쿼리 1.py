def solution(arr, queries):
    for i in range(len(queries)):
        s, e = queries[i]
        for l in range(s, e+1):
            arr[l] += 1
    
    return arr