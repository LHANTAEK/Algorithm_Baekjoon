def solution(array, commands):
    answer = []
    for l in commands:
        i, j, k = l
        array_sliced = array[i-1:j]
        array_sorted = sorted(array_sliced)
        answer.append(array_sorted[k-1])
    return answer