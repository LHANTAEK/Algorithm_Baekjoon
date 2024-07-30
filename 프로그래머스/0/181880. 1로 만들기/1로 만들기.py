def solution(num_list):
    answer = 0
    while True:
        
        for i in range(len(num_list)):
            if num_list[i] % 2 == 0:
                num_list[i] /= 2
                answer += 1
            elif num_list[i] % 2 == 1 and num_list[i] != 1:
                num_list[i] = (num_list[i] - 1) / 2
                answer += 1
                
        if sum(num_list) == len(num_list):
            break
            
    return answer