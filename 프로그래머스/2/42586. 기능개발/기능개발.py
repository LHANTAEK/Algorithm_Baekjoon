import math

def solution(progresses, speeds):
    answer = []
    days = []
    
    for i in range(len(progresses)):
        days.append(math.ceil((100 - progresses[i]) / speeds[i]))
    
    max_day = days[0]
    count = 0
        
    for day in days:
        if day > max_day:
            answer.append(count)
            count = 1
            max_day = day
        else:
            count += 1
            
    answer.append(count)
            
    return answer