def solution(my_string, alp):
    answer = ''
    for i in range(len(my_string)):
        if my_string[i] == alp:
            answer = my_string.replace(alp, alp.upper())
        elif alp not in my_string:
            answer = my_string
    return answer