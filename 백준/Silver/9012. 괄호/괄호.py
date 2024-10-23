for i in range(int(input())):
    stk = []
    is_valid = True
    s = input()
    
    for char in s:
        if char == '(':
            stk.append(char)
        else:
            if not stk:
                is_valid = False
                break
            stk.pop()
            
    print('YES' if is_valid and not stk else 'NO')