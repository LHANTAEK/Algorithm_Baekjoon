import sys

N = int(input())

input = sys.stdin.read

N_list = list(map(int, input().split()))

result = sorted(N_list, key=lambda x: x)

for l in result:
    print(l)