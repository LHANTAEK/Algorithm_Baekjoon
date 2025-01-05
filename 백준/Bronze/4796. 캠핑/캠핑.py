import sys

input = sys.stdin.readline
case = 0

while True:
    L, P, V = map(int, input().split())
    
    if L == 0:
        break
    
    case += 1
    a = V // P
    b = min(V % P, L)

    answer = a * L + b
    print(f"Case {case}: {answer}")