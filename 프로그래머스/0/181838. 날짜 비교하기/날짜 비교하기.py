def solution(date1, date2):
    answer = 0
    str_date1 = ''
    str_date2 = ''
    for i in date1:
        str_date1 += str(i)
    for l in date2:
        str_date2 += str(l)
    if int(str_date1) < int(str_date2):
        answer = 1
    else:
        answer = 0
    return answer