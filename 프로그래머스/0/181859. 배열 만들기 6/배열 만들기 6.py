def solution(arr):
    other = [-1]
    stk = []
    i = 0
    while i < len(arr):
        if  len(stk) == 0:
            stk.append(arr[i])
            i += 1
            
        elif len(stk) != 0 and stk[-1] == arr[i]:
            del stk[-1]
            i += 1
            
        elif len(stk) != 0 and stk[-1] != arr[i]:
            stk.append(arr[i])
            i += 1
        
            
    return stk if stk else other