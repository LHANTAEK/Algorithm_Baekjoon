from collections import Counter

N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

count = Counter(N_list)

answer = [count[i] for i in M_list]
print(' '.join(map(str, answer)))