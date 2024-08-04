def solution(strArr):
    from collections import Counter
    
    len_list = []
    
    for i in strArr:
        len_list.append(len(i))
    
    Counter_list = Counter(len_list)
    answer = list(Counter_list.values())
    
    return max(answer)