def solution(chicken):
    answer = 0
    coupon = chicken
    
    while coupon >= 10:
        new_chicken = coupon // 10
        answer += new_chicken
        coupon = (coupon % 10) + new_chicken
    return answer