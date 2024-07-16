def solution(arr, queries):
    for l in range(len(queries)):
        s, e, k = queries[l]
        for i in range(s,e+1):
            if i % k == 0:
                arr[i] += 1
                
    return arr

        
