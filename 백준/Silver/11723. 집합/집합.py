import sys

input = sys.stdin.readline

M = int(input())

S = set()

for _ in range(M):
    precommand = input().rstrip()
    # print(precommand)
    if precommand == "all":
        S = set(range(1,21))
        
    elif precommand == "empty":
        S = set()
    
    else:
        # print(precommand)
        command, num = precommand.split()
        num = int(num)
        
        if command == "add":
            S.add(num)
        elif command == "remove":
            if num not in S:
                pass
            else:
                S.remove(num)
        elif command == "check":
            print( 1 if num in S else 0)
        elif command == "toggle":
            if num in S:
                S.remove(num)
            else:
                S.add(num)