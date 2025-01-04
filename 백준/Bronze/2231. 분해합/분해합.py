N = int(input())
answer = 0

for i in range(N//2, N+1):
    num_sum = sum(list(map(int, str(i))))
    result = num_sum + i
    
    if result == N:
        answer = i
        print(answer)
        break
    
if not answer:
    print(0)