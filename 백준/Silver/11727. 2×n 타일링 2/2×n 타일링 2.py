n = int(input())
rect = [0] * 1001
rect[1] = 1

if n >= 2:
    rect[2] = 3
    for i in range(3, n+1):
        rect[i] = (rect[i-2]*2) + rect[i-1]
        
print(rect[n]%10007)