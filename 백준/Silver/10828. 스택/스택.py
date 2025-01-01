import sys

N = int(input())
lines = sys.stdin.readlines()
stack = []

for line in lines:
    command = line.split()
    sign = command[0]
    
    if sign == "push":
        stack.append(int(command[1]))
    elif sign == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif sign == "size":
        print(len(stack))
    elif sign == "empty":
        print(1 if not stack else 0)
    elif sign == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)