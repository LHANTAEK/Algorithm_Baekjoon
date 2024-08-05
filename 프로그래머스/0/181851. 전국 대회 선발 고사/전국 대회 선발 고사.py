def solution(rank, attendance):
    answer = 0
    result = []
    result_index = []
    
    for i in range(len(attendance)):
        if attendance[i] == True:
            result.append([i, rank[i]])
    result = sorted(result, key = lambda x: x[1])
    result = result[:3]
        
    for l in result:
        p, q = l
        result_index.append(p)
    
    a, b, c= result_index
    
    answer = 10000 * a + 100 * b + c
        
        
        
    return answer