import sys
input = sys.stdin.readline

N, M = map(int, input().split())
N_set = set()
M_set = set()

for _ in range(N):
    N_set.add(input().rstrip())
    
for _ in range(M):
    M_set.add(input().rstrip())
    
ans = sorted(N_set & M_set)

print(len(ans))

for i in ans:
    print(i)