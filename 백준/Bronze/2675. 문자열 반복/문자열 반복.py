T = int(input())

for _ in range(T):
    answer = ''
    a, b = input().split()
    a = int(a)
    answer = ''.join([char * a for char in b])
    print(answer)