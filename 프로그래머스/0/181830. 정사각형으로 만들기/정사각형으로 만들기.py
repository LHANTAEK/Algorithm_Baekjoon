def solution(arr):
    
    if len(arr) > len(arr[0]):
        p = len(arr) - len(arr[0])
        for i in range(len(arr)):
            arr[i].extend([0]*p)
        return arr
    elif len(arr) < len(arr[0]):
        k = len(arr[0]) - len(arr)
        while k > 0:
            arr.append(([0]*len(arr[0])))
            k -= 1
        return arr
    else:
        return arr
        
    