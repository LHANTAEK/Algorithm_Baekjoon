def solution(arr):
    
    power_of_two = []
    
    for i in range(0,11):
        power_of_two.append(2**i)
    
    if len(arr) in power_of_two:
        return arr
    
    else:
        while True:
            arr.append(0)
            if len(arr) in power_of_two:
                return arr

            