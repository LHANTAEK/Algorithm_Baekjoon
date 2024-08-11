def solution(array):
    from collections import Counter
    answer = 0
    counter_array = Counter(array)
    array_top2 = counter_array.most_common(2)
    if len(array_top2) >= 2:
        if array_top2[0][1] == array_top2[1][1]:
            answer = -1
        else:
            answer = counter_array.most_common(1)[0][0]
    else:
        answer = counter_array.most_common(1)[0][0]
    
    return answer
