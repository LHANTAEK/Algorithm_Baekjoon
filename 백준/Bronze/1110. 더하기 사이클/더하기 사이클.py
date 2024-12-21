N = int(input())
origin = N
count = 0

while True:
    count += 1
    a = N // 10
    b = N % 10
    c = (a + b) % 10
    N = b * 10 + c
    
    if N == origin:
        print(count)
        break