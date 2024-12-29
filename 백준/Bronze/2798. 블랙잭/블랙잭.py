from itertools import combinations

N, M = map(int, input().split())
C3_sum_list = list(combinations(list(map(int, input().split())), 3))
answer_list = []
result_list = []

for i in C3_sum_list:
    answer_list.append(sum(i))

for l in answer_list:
    if l <= M:
        result_list.append(l)
        
result = sorted(result_list)
print(result[-1])