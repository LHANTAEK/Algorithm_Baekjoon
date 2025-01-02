import sys

N = list(map(int, sys.stdin.readlines()))
a, b, c = N

print(a+b-c)
print(int(f"{a}{b}")-c)