from math import gcd

N, M = map(int, input().split())
G = gcd(N,M)

print(G)
print((N//G) * (M//G) * G)