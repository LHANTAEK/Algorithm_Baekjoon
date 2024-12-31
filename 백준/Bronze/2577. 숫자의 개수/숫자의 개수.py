import sys

a, b, c = map(int, sys.stdin.readlines())
N = a * b * c
num_dict = {str(l) : 0 for l in range(10)}

for i in str(N):
    if i not in num_dict:
        num_dict[i] = 1
    else:
        num_dict[i] += 1
        
for k in num_dict:
    print(num_dict[k])