def solution(intStrs, k, s, l):
    answer = []
    for i in range(len(intStrs)):
        target = intStrs[i]
        Strs_Int = int(target[s:s+l])
        if Strs_Int > k:
            answer.append(Strs_Int)
    return answer