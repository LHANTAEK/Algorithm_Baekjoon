def solution(myString, pat):
    answer = ''
    text_start_index = myString.rfind(pat)
    answer = myString[:text_start_index+len(pat)]
    return answer