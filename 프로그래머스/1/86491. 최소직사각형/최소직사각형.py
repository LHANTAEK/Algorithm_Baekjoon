def solution(sizes):
    max_width = 0
    max_height = 0
    
    for card in sizes:
        # 각 명함의 긴 쪽을 가로로, 짧은 쪽을 세로로 재배치
        width, height = max(card), min(card)
        
        # 현재까지의 최대 가로, 세로 길이와 비교하여 갱신
        max_width = max(max_width, width)
        max_height = max(max_height, height)
    
    # 가장 큰 가로 길이와 세로 길이를 곱하기
    return max_width * max_height
