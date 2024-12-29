import math

N = int(input())
size_list = map(int, input().split())
t_bundle, p_bundle = map(int, input().split())
t_order_number = 0

for i in size_list:
    t_order_number += math.ceil(i / t_bundle)

print(t_order_number)
print(N//p_bundle, N%p_bundle)