import sys
input = sys.stdin.readline
n, m = map(int, input().split())
result = [[int(x) for x in input().rstrip()] for _ in range(n)]

dp = [[0] * m for _ in range(n)]
dp[0] = result[0]

for i in range(n):
    dp[i][0] = result[i][0]
    
for i in range(1, n):
    for j in range(1, m):
        if result[i][j] == 1:
            dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1

# 한 변의 길이를 구한 후 넓이를 계산
side_length = max(map(max, dp))
print(side_length * side_length)