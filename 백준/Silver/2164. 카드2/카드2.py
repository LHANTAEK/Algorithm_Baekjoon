from collections import deque

dq = []

for i in range(1, int(input()) + 1):
    dq.append(i)

dq_result = deque(dq)

while len(dq_result) > 1:
    dq_result.popleft()
    dq_result.rotate(-1)

print(dq_result[0])