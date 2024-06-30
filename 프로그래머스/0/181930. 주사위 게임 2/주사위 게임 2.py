def solution(a, b, c):
    answer = 0
    if a != b and a != c and b != c:
        answer = a + b + c
    elif (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
        answer = (a + b + c) * (a**2 + b**2 + c**2)
    else:
        answer = (a + b + c) * (a**2 + b**2 + c**2) * (a**3 + b**3 + c**3)
    return answer

# set은 중복되는 원소가 있을 때 하나만 적게하므로 이렇게 사용해서 문제를 풀 수도 있다.

# def solution(a, b, c):
#     check=len(set([a,b,c]))
#     if check==1:
#         return 3*a*3*(a**2)*3*(a**3)
#     elif check==2:
#         return (a+b+c)*(a**2+b**2+c**2)
#     else:
#         return (a+b+c)
