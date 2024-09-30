from collections import Counter

def solution(before, after):
    answer = 0
    before_counter = Counter(before)
    after_counter = Counter(after)
    
    if before_counter == after_counter:
        answer = 1
    else:
        answer = 0
    return answer