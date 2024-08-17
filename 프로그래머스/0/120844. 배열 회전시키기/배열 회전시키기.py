def solution(numbers, direction):
    
    if direction == "right":
        a = numbers.pop()
        numbers.insert(0, a)
    else:
        b = numbers[0]
        del numbers[0]
        numbers.insert(len(numbers), b)
    return numbers