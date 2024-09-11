def solution(dots):
    answer = 0
    def slope(dot1, dot2):
        x1, y1 = dot1
        x2, y2 = dot2
        return (y2 - y1) / (x2 - x1)
    
    slopes = [
        (dots[0], dots[1], dots[2], dots[3]),
        (dots[0], dots[2], dots[1], dots[3]),
        (dots[0], dots[3], dots[1], dots[2])
    ]
    
    for dot1, dot2, dot3, dot4 in slopes:
        if slope(dot1, dot2) == slope(dot3, dot4):
            return 1
    return 0