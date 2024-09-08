def solution(my_string):
    answer = 0
    answer_str_list = ""
    for i in my_string:
        if not i.isalpha():
            answer_str_list += i
        else:
            if answer_str_list:
                answer += int(answer_str_list)
                answer_str_list = ""
    if answer_str_list:
        answer += int(answer_str_list)
    return answer