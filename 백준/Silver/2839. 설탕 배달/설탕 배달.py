N = int(input())
sugar3, sugar5 = 3, 5
min_bags = float('inf')

for count5 in range(N // sugar5 + 1):
    remaining = N - (count5 * sugar5)
    
    if remaining % sugar3 == 0:
        count3 = remaining // 3
        min_bags = min(min_bags, count5 + count3)
        
if min_bags == float('inf'):
    print(-1)
else:
    print(min_bags)