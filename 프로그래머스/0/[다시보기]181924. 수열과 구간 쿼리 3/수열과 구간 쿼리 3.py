def solution(arr, queries):
    for query in queries:
        i, j = query
        arr[i], arr[j] = arr[j], arr[i]
    return arr

# 파이썬의 튜플 언패킹 기능을 사용하면 리스트나 튜플의 값을 여러 변수에 한 번에 할당할 수 있습니다.
# 이를 통해 코드가 더 간결하고 가독성이 높아집니다.
# 리스트도 튜플처럼 언패킹할 수 있습니다. i, j = query는 query가 [i, j] 형태일 때 유효합니다.
