def solution(emergency):
    answer = []
    answer_list = list(enumerate(emergency))
    sorted_emergency = sorted(answer_list, key=lambda x: x[1], reverse = True)
    answer = [0] * len(emergency)
    
    for rank, (index, _) in enumerate(sorted_emergency, 1):
        answer[index] = rank
    
    return answer