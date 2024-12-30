import sys

input = sys.stdin.readline

N = int(input())
answer_list = []

for i in range(N):
    X, Y = map(int, input().split())
    answer_list.append([X,Y])

answer = sorted(answer_list, key=lambda x: (x[0], x[1]))

for l in answer:
    print(f"{l[0]} {l[1]}")