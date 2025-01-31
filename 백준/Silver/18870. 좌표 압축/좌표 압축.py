import sys

input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))

set_nums = sorted(set(nums))

dic_nums = {}
for index, num in enumerate(set_nums):
    dic_nums[num] = index
    
for i in nums:
    print(dic_nums[i], end=" ")