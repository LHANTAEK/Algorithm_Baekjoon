import math

def solution(a, b):
    answer = 0
    gcd = math.gcd(a,b)
    reduced_b = b // gcd
    
    while reduced_b % 2 == 0:
        reduced_b //= 2
    while reduced_b % 5 == 0:
        reduced_b //= 5
        
    if reduced_b == 1:
        answer = 1
    else:
        answer = 2
    return answer