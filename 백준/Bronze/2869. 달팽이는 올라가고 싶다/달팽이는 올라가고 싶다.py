def f(A, B, V):
    daily_progress = A - B
    
    import math
    days = math.ceil((V-A) / daily_progress) + 1
    
    return days

A, B, V = map(int, input().split())
print(f(A,B,V))