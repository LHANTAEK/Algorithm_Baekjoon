from math import factorial

N = int(input())
fac_N = factorial(N)
cnt = 0

for i in str(fac_N)[::-1]:
    if i == "0":
        cnt += 1
        continue
    else:
        print(cnt)
        exit(0)