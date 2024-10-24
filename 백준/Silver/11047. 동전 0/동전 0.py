N, K = map(int, input().split())

coins = sorted(
    [int(input()) for _ in range(N)],
      reverse=True
      )

coins = [coin for coin in coins if coin <= K]

if K in coins:
    print(1)
else:
    result = 0

    for coin in coins:
        result += K // coin # 코인 개수 
        K = K % coin # 나머지 
        if K == 0:
            break

    print(result if K == 0 else 0)