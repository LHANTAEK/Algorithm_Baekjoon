T = int(input())

for i in range(T):
    a, b, c = map(int, input().split())
    
    floor = c % a
    room_number = (c // a) + 1
    
    if floor == 0:
        floor = a
        room_number -= 1
    
    print(f"{floor}{room_number:02d}")