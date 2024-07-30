# def solution(num_list):
#     answer = 0
#     if len(num_list) >= 11:
#         answer = sum(num_list)
#     else:
#         for i in range(1, len(num_list)):
#             num_list[i] = num_list[i] * num_list[i-1]
#             answer = num_list[-1]
#     return answer


# 다른 풀이
def solution(num_list):
    if len(num_list) >= 11:
        answer = eval('+'.join(list(map(str, num_list))))
        return answer
    else:
        answer = eval('*'.join(list(map(str, num_list))))
        return answer