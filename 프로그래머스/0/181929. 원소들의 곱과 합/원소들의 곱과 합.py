# def multiply(num_list):
#     return eval('*'.join(str(n) for n in num_list))

# def sum_sum(num_list):
#     return (sum(num_list)**2)

# def solution(num_list):
#     answer = 0
#     return (1 if multiply(num_list) < sum_sum(num_list) else 0)


# 다른 풀이
def solution(num_list):
    a=1
    b=0
    for x in num_list:
        a*=x
        b+=x
    if a<b*b: return 1
    return 0

def solution(num_list):
    a = 1
    b = 0
    for x in num_list:
        a *= x
        b += x
    if a < b**2:
        return 1
    else:
        return 0