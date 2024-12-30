N = int(input())
answer_list = []

for i in range(N):
    age, name = input().split()
    answer_list.append([int(age), name, i])
    
result = sorted(answer_list, key=lambda x : (int(x[0]), x[2]))

for l in result:
    print(f"{l[0]} {l[1]}")