def solution(my_string, m, c):
    answer = []
    real_answer = ''
    for i in range(0, len(my_string), m):
        answer.append(my_string[i:i+m])
    for l in range(len(answer)):
        real_answer += answer[l][c-1]
    return real_answer



# a = "ihrhbakrfpndopljhygc"
# answer = []
# real_answer = ""
# for i in range(0, len(a), 4):
#     answer.append(a[i:i+4])
# for l in range(len(answer)):
#     real_answer += answer[l][1]
# print(real_answer)