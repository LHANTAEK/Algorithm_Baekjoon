def solution(n, lost, reserve):
    answer = 0
    n_dict = {i: 1 for i in range(1, n+1)}
    
    for l in reserve:
        if l in n_dict:
            n_dict[l] += 1
            
    for k in lost:
        if k in n_dict:
            n_dict[k] -= 1
            
    for j in range(1, n+1):
        if j == 1:
            if n_dict[j] == 0:
                if n_dict[j+1] == 2:
                    n_dict[j+1] -= 1
                    n_dict[j] += 1
        elif j != n:
            if n_dict[j] == 0:
                if n_dict[j-1] == 2:
                    n_dict[j-1] -= 1
                    n_dict[j] += 1
                elif n_dict[j+1] == 2:
                    n_dict[j+1] -= 1
                    n_dict[j] += 1
        else:
            if n_dict[j] == 0:
                if n_dict[j-1] == 2:
                    n_dict[j-1] -= 1
                    n_dict[j] += 1
                
    for h in range(1, n+1):
        if n_dict[h] >= 1:
            answer += 1

    return answer