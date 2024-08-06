def solution(picture, k):
    result = []
    for row in picture:
        expanded_row = ''
        for char in row:
            expanded_row += char * k
        for _ in range(k):
            result.append(expanded_row)
    return result
