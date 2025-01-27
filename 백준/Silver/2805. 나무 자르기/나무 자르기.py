import sys
input = sys.stdin.readline

N, M = map(int, input().split())
woods = list(map(int, input().split()))
start = 0
end = max(woods)

result = 0
while start <= end:
    mid = (start + end) // 2
    total = sum(tree - mid if tree > mid else 0 for tree in woods)
    
    if total >= M:
        result = mid
        start = mid + 1
    else:
        end = mid - 1

print(result)