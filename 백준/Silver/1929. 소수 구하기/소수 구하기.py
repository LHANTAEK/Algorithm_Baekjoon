def is_prime(n: int) -> bool:
    
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    for i in range(5, int(n**0.5) + 1, 2): # 홀수만 확인
        if n % i == 0:
            return False
        
    return True


a, b = map(int, input().split())

for n in range(a, b + 1):
    if is_prime(n):
        print(n)        