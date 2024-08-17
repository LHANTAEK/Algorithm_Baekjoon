def solution(numbers, direction):
    
    if direction == "right":
        a = numbers.pop()
        numbers.insert(0, a)
    else:
        b = numbers[0]
        del numbers[0]
        numbers.insert(len(numbers), b)
    return numbers



# collections 함수의 deque를 이용해서 풀 수도 있더라..
from collections import deque

def solution(numbers, direction):

    numbers = deque(numbers)

    if direction == 'right':
        numbers.rotate(1)
        return list(numbers)
    else:
        numbers.rotate(-1)
        return list(numbers)
