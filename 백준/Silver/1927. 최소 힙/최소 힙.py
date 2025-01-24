import heapq
import sys

input = sys.stdin.read
data = input().splitlines()

n = int(data[0])  # 연산의 개수
commands = data[1:]  # 나머지 연산들

min_heap = []
result = []

for command in commands:
    x = int(command)
    if x == 0:
        if min_heap:
            result.append(heapq.heappop(min_heap))
        else:
            result.append(0)
    else:
        heapq.heappush(min_heap, x)

# 출력 결과
for r in result:
    print(r)
