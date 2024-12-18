N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

N_set = set(N_list)

answer = []

for item in M_list:
    if item in N_set:
        answer.append(1)
        N_set.remove(item)
    else:
        answer.append(0)
    
        
print(' '.join(map(str, answer)))