from collections import Counter

name = input()
counter = Counter(name)
odd_num = 0
half = []
mid = ''

for k, v in sorted(counter.items()): 
    if v % 2:
        odd_num += 1
        mid = k
        if odd_num >= 2:
            print("I'm Sorry Hansoo")
            exit()
            
    half.extend([k] * (v//2))
    
result = ''.join(half) + mid + ''.join(half[::-1])
print(result)