def solution(dots):
    answer = 0
    dots.sort(key=lambda x: x[0])
    x = dots[3][0] - dots[0][0]
    dots.sort(key=lambda x: x[1])
    y = dots[3][1] - dots[0][1]
    answer = x * y
    return answer