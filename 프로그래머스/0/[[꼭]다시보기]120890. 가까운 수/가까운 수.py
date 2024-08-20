def solution(array, n):
    answer = 0
    array.sort(key=lambda x: (abs(n-x), x))
    return array[0]
