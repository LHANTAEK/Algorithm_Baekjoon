def solution(myString):
    test = ''
    answer = myString.lower()
    for i in range(len(answer)):
        if answer[i] == "a":
            test += answer[i].replace("a","A")
        else:
            test += answer[i]
    return test