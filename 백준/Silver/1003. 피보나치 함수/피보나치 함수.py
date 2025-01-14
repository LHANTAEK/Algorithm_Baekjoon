N = int(input())
for _ in range(N):
    N = int(input())
    zero, one = 1, 0
    for i in range(N):
        zero, one = one, zero + one
    print(f"{zero} {one}")