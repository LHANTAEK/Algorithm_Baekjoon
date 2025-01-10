import sys
input = sys.stdin.readline

N = int(input())
num_list = []

for _ in range(N):
    weight, height = map(int, input().split())
    num_list.append((weight, height))
    
for i in num_list:
    rank = 1
    for j in num_list:
        if i[0] < j[0] and i[1] < j[1]:
            rank += 1
    print(rank, end=" ")