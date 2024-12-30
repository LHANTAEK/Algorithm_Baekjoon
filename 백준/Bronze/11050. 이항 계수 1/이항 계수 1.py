from itertools import combinations

N, K = map(int, input().split())

N_list = [i for i in range(N)]

print(len(list(combinations(N_list, K))))