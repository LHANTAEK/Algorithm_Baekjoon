def solution(n):
    answer_list = []
    for i in range(1,301):
        if i % 3 != 0 and '3' not in str(i):
            answer_list.append(i)
    return answer_list[n-1]