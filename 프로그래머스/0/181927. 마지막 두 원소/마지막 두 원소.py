def solution(num_list):
    answer = []
    i = len(num_list) - 1
    
    if num_list[i] > num_list[i-1]:
        for n in range(i+1):
            answer.append(num_list[n])
        answer.append(num_list[i] - num_list[i-1])
    else:
        for n in range(i+1):
            answer.append(num_list[n])
        answer.append(num_list[i] * 2)    
    return answer