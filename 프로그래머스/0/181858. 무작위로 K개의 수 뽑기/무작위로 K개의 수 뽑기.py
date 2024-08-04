def solution(arr, k):
    set_arr = list(dict.fromkeys(arr))
    
    if len(set_arr) < k:
        set_arr.extend([-1]* (k-len(set_arr)))
            
    else:
        set_arr = set_arr[:k]
            
    return set_arr
               