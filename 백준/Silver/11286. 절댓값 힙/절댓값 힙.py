import heapq as hq
import sys

result = []

for i in range(int(input())):
    a = int(sys.stdin.readline())
    if a != 0:
        hq.heappush(result, [abs(a), a])
    else:
        if len(result) == 0:
            print(0)
        else:
            print(hq.heappop(result)[1])