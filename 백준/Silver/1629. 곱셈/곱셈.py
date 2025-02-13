import sys
sys.setrecursionlimit(10**6)

def power(a,b,c):
    if b == 0:
        return 1
    if b == 1:
        return a % c
    
    temp = power(a, b//2, c)
    
    if b % 2:
        return (temp * temp * a) % c
    else:
        return (temp * temp) % c
    
A, B, C = map(int, input().split())
print(power(A,B,C))