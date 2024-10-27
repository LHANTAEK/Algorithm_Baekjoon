# math 라이브러리의 최대공약수를 구하는 gcd 모듈을 통해서 쉽게 풀이 가능
def solution(numer1, denom1, numer2, denom2):
    import math
    
    numer = numer1 * denom2 + numer2 * denom1
    denom = denom1 * denom2
    gcd = math.gcd(numer, denom)
    
    return [numer / gcd, denom / gcd]




# 유클리드 알고리즘 // import math ... math.gcd 없이 최대공약수 구하는 알고리즘
# def gcd(a, b):
#     while b:
#         a, b = b, a % b
#     return a


# 처음 풀이
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
