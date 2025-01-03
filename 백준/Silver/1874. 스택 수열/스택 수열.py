N = int(input())
target = [int(input()) for i in range(N)]

current = 1 # 다음에 push할 수
stack = [] # 스택
result = [] # 연산 기록 -> 최종 답

for num in target:
    
    while current <= N and (not stack or stack[-1] < num):
        stack.append(current)
        result.append("+")
        current += 1
        
    if stack and stack[-1] == num:
        stack.pop()
        result.append("-")
    else:
        print("NO")
        exit(0)
        
print('\n'.join(result))