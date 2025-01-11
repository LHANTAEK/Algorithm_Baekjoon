K = int(input())
ans = []

for _ in range(K):
    num = int(input())
    
    if num != 0:
        ans.append(num)
    elif num == 0:
        ans.pop()
        
print(sum(ans))