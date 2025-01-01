from collections import deque

N, K = map(int, input().split())
answer_list = deque(range(1, N+1))
result = []

while answer_list:
    answer_list.rotate(-(K-1))
    result.append(answer_list.popleft())

answer = ', '.join(map(str, result))

print(f"<{answer}>")