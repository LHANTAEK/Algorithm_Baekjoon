def solution(a, b, c, d):
    answer = 0
    dice = [a,b,c,d]
    dice.sort()
    
    if dice[0] == dice [1] == dice[2] == dice[3]:
        answer = 1111 * dice[0]
    
    elif dice[0] == dice [1] == dice[2] or dice[1] == dice [2] == dice[3]:
        if dice[0] == dice [1]:
            p = dice[0]
            q = dice[3]
        elif dice[0] != dice[1]:
            p = dice[3]
            q = dice[0]
        answer = ((10 * p) + q)**2
        # 같은게 두 쌍일 때
    elif dice[0] == dice[1] != dice[2] and dice[2] == dice[3] != dice[1]:
        p = dice [0]
        q = dice[2]
        answer = (p + q) * abs(p - q)
    elif (dice[0] == dice[1] != dice[2] and dice[2] != dice[3]) or (dice[1] == dice[2] != dice[0] != dice[3] or (dice[2] == dice[3] != dice[0] != dice[1])):
        if dice[0] == dice[1]:
            q = dice[2]
            r = dice[3]
            answer = q * r
        elif dice[1] == dice[2]:
            q = dice[0]
            r = dice[3]
            answer = q * r
        else:
            q = dice[0]
            r = dice[1]
            answer = q * r
    else:
        answer = min(a,b,c,d)
        
        
    return answer
