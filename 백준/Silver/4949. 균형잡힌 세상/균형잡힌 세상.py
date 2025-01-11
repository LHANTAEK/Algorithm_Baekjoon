import sys
input = sys.stdin.readline

while True:
    dis = []
    obj = input().rstrip()

    if obj == ".":
        break
    balance = True
    
    for i in obj:
        if i == "(" or i == "[":
            dis.append(i)
        elif i == ")":
            if dis and dis[-1] == "(":
                dis.pop()
            else:
                balance = False
                break
        elif i == "]":
            if dis and dis[-1] == "[":
                dis.pop()
            else:
                balance = False
                break
    
    if balance and not dis:
        print("yes")
    else:
        print("no")