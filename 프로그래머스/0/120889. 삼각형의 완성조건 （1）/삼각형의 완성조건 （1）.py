def solution(sides):
    answer = 0
    sides_max = max(sides)
    sides.remove(sides_max)
    
    if sides_max >= sum(sides):
        answer = 2
    else:
        answer = 1
    return answer