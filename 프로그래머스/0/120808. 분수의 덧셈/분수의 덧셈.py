def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def solution(numer1, denom1, numer2, denom2):
    # 분모의 최소공배수 계산
    lcm = (denom1 * denom2) // gcd(denom1, denom2)
    
    # 분자 계산
    numer = (numer1 * (lcm // denom1)) + (numer2 * (lcm // denom2))
    denom = lcm
    
    # 기약분수로 만들기
    divisor = gcd(numer, denom)
    numer //= divisor
    denom //= divisor
    
    return [numer, denom]

# def solution(numer1, denom1, numer2, denom2):
#     answer = []
#     if denom1 % denom2 == 0 or denom2 % denom1 == 0:
#         if denom1 % denom2 == 0:
#             answer += [numer1 + numer2*(denom1//denom2), denom1]
#             return answer
#         elif denom2 % denom1 == 0:
#             answer += [numer2 + numer1*(denom2//denom1), denom2]
#             return answer

#     else:
#         answer += [numer1 * denom2 + numer2 * denom1, denom1 * denom2]
#         return answer