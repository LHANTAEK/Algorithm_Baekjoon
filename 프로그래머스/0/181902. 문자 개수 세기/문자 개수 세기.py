def solution(my_string):
    answer = []
    dic = {}
    for i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz':
        dic[i] = 0
        
    for i in my_string:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
            
    answer = list(dic.values())

    return answer
