def solution(myString):
    answer = []
    result = myString.split('x')
    for i in result:
        if not len(i) == 0:
            answer.append(i)
            answer.sort()
    return answer