def solution(balls, share):
    answer = 0
    bunja = 1
    bunmo = 1
    for i in range(balls-share+1, balls+1):
        bunja *= i
    for l in range(1, share+1):
        bunmo *= l
    answer = bunja / bunmo
    return answer