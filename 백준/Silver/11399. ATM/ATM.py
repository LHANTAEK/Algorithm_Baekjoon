N = int(input())
nums = list(map(int, input().split()))
nums = sorted(nums)

sums = 0
ans = []

for i in nums:
    sums += i
    ans.append(sums)
    
print(sum(ans))