N = int(input())
num_list = list(map(int, input().split()))
result = 0

for i in num_list:
    length = 0
    for l in range(1, i+1):
        if i % l == 0:
            length += 1
    if length == 2:
        result += 1

print(result)