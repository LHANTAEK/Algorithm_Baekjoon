N = int(input())
number_list = [0] * 91
number_list[0] = 0
number_list[1] = 1

for i in range(2, N+1):
    number_list[i] = number_list[i-1] + number_list[i-2]

print(number_list[N])