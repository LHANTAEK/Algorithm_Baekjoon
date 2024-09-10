def solution(board):
    n = len(board)
    
    # 위험 지역을 표시할 배열을 생성
    danger_zone = [[False] * n for _ in range(n)]
    
    # 지뢰의 주변 8칸을 체크하는 방향 벡터
    directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]
    
    # 지뢰가 있는 지역의 주변을 모두 위험 지역으로 설정
    for i in range(n):
        for j in range(n):
            if board[i][j] == 1:  # 지뢰가 있으면
                # 자신 위치도 위험 지역으로 설정
                danger_zone[i][j] = True
                # 주변 8방향을 위험 지역으로 설정
                for dx, dy in directions:
                    ni, nj = i + dx, j + dy
                    if 0 <= ni < n and 0 <= nj < n:
                        danger_zone[ni][nj] = True
    
    # 안전한 지역(위험 지역이 아닌 0인 지역)을 카운트
    safe_count = 0
    for i in range(n):
        for j in range(n):
            if not danger_zone[i][j] and board[i][j] == 0:
                safe_count += 1
    
    return safe_count
