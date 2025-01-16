def calculate_combinations(n):
    # 동적 프로그래밍을 위한 배열 초기화
    # n이 11보다 작다고 했으므로 크기 12로 초기화
    dp = [0] * 12
    
    # 기본 케이스 초기화
    dp[1] = 1  # 1을 만드는 방법: 1
    dp[2] = 2  # 1+1, 2
    dp[3] = 4  # 1+1+1, 1+2, 2+1, 3
    
    # n이 4이상인 경우 점화식 적용
    for i in range(4, n + 1):
        dp[i] = dp[i-1] + dp[i-2] + dp[i-3]
    
    return dp[n]

t = int(input())

for _ in range(t):
    n = int(input())
    print(calculate_combinations(n))