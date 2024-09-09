def solution(sides):
    answer = 0
    answer_list = []
    sides.sort(reverse=True)
    a, b = sides
    
    for i in range(1, a+b+1):
        if b + i > a and i <= a:
            answer_list.append(i)
        elif i > a and i <= a + b:
            answer_list.append(i)
            
    return len(answer_list) - 1