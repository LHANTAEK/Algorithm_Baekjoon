def solution(my_strings, parts):
    answer = ''
    for i in range(len(my_strings)):
        s, e = parts[i]
        allocated_string = my_strings[i]
        answer += allocated_string[s:e+1]
    return answer