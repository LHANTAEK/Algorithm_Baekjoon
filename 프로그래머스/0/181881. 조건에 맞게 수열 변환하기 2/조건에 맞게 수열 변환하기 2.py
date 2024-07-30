def solution(arr):
    answer = 0

    while True:
        new_arr = []
        
        for i in range(len(arr)):
            if arr[i] >= 50 and arr[i] % 2 == 0:
                new_arr.append(arr[i] / 2)
            elif arr[i] < 50 and arr[i] % 2 == 1:
                new_arr.append(arr[i] * 2 + 1)
            else:
                new_arr.append(arr[i])
                
            
        if new_arr == arr:
            break
            
        arr = new_arr
        answer += 1
        
    return answer