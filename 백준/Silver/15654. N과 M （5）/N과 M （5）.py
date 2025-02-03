from itertools import permutations

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))

perm = list(permutations(nums, M))

for i in perm:
    for l in i:
        print(l, end=" ")
    print(end="\n")