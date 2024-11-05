N, L = map(int, input().split())
leak_list = [False] * 1001

for i in map(int, input().split()):
    leak_list[i] = True
    
cursor = 0
result = 0

while cursor < 1001:
    if leak_list[cursor]:
        result += 1
        cursor += L
    else:
        cursor += 1

print(result)