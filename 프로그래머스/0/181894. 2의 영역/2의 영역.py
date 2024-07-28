def solution(arr):
    position = [i for i, x in enumerate(arr) if x == 2]
    
    if not position:
        return [-1]
    
    start = position[0]
    end = position[-1]
    
    answer = arr[start:end+1]
    
    return answer