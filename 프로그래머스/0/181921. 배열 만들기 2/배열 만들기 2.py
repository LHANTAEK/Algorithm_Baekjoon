def solution(l, r):
    answer = []
    for i in range(l, r+1):
        i_str = str(i)
        if all(char in '05' for char in i_str):
            answer.append(i)
    if not answer:
        return [-1]
    
    return answer