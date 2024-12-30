N = int(input())
str_list = []

for _ in range(N):
    str_list.append(input())
    
result = sorted(set(str_list), key=lambda x: (len(x), x))

for i in result:
    print(i)