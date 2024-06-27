def solution(a, b):
    answer = 0
    if int(str(a)+str(b)) >= 2 * a * b:
        answer = int(str(a) + str(b))
    else:
        answer = 2 * a * b
    return answer

# max 모듈을 쓰면 쉽다!
# 쓰면 된다는 걸 알았지만 처음에 아래와 같이 작성함


# 1번 풀이
# def solution(a,b):
#     return int(max(f"{a}{b}", f"{2*a*b}")) ...... NO, 문자열간 max 메소드는 문자열이 빠른 순으로 나타나기 때문에 a = 1, b= 2의 경우처럼 문제에서 요구하는 바와 결과값이 달라질 수 있다. 따라서 다음과 같이 작성해야 한다.
#     return max(int(f"{a}{b}), int(f"{2*a*b}))...... OK!

# 2번 풀이
# def solution(a,b):
#     return max(int(str(a) + str(b)), 2 * a * b)

