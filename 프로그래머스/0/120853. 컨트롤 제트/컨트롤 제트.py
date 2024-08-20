def solution(s):
    answer = 0
    s_list = s.split(' ')
    for i in range(len(s_list)):
        if not s_list[i] == 'Z':
            answer += int(s_list[i])
        else:
            answer += -int(s_list[i-1])

    return answer


# def solution(s):
#     answer = 0
#     answer_list = []
#     s_list = s.split(' ')
#     for i in range(len(s_list)):
#         if s_list[i] == 'Z' and int(s_list[i-1]) > 0:
#             answer_list.append(("-" + s_list[i-1]))
#         elif s_list[i] == 'Z' and int(s_list[i-1]) < 0 :
#             answer_list.append(s_list[i-1])
#         else:
#             answer_list.append(s_list[i])
#     for l in answer_list:
#         answer += int(l)
    
#     return answer