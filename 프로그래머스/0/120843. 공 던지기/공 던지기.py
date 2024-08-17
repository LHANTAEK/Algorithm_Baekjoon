def solution(numbers, k):
    from collections import deque
    numbers = deque(numbers)
    numbers.rotate(-2 * (k-1))
    numbers = list(numbers)
        
    return numbers[0]