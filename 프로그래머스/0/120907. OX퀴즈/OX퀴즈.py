def solution(quiz):
    answer = []
    for i in quiz:
        split_list = i.split('=')
        if eval(split_list[0]) == eval(split_list[1]):
            answer.append("O")
        else:
            answer.append("X")
    return answer