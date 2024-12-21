N = int(input())
score_list = list(map(int, input().split()))
M = max(score_list)
result = []

for i in score_list:
    result.append((i/M) * 100)
        
print(sum(result)/N)