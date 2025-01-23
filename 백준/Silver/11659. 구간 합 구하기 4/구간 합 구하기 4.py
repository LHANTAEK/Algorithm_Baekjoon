import sys
input = sys.stdin.readline
N, M = map(int, input().split())

nums = list(map(int, input().split()))
prefix = [0] * (N+1)

for i in range(N):
    prefix[i+1] = prefix[i] + nums[i]

for _ in range(M):
    i, j = map(int, input().split())
    print(prefix[j] - prefix[i-1])