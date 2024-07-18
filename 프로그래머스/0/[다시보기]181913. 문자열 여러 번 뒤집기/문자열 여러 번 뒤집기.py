def solution(my_string, queries):
    # 각 쿼리마다 my_string을 변형
    for query in queries:
        s, e = query
        # my_string을 s부터 e까지 뒤집고 그 전후의 부분과 합침
        my_string = my_string[:s] + my_string[s:e+1][::-1] + my_string[e+1:]
    return my_string
