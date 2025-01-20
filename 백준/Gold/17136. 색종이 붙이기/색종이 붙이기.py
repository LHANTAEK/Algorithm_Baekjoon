paper = [list(map(int, input().split())) for _ in range(10)]
remain = [5] * 5 # 각 크기별 색종이 남은 개수 (인덱스 0~4가 1~5 크기를 의미)
answer = float('inf')

def check(x, y, size):
    # 격자를 벗어나는지 확인
    if x + size > 10 or y + size > 10:
        return False
    
    # size x size 영역이 모두 1인지 확인
    for i in range(x, x + size):
        for j in range(y, y + size):
            if paper[i][j] != 1:
                return False
    return True

def put(x, y, size, val):
    for i in range(x, x + size):
        for j in range(y, y + size):
            paper[i][j] = val
            
def dfs(x, y, cnt):
    global answer
    
    # 현재 개수가 이미 찾은 최소값보다 크다면 더 볼 필요가 없음
    if cnt >= answer:
        return
    
    # 끝까지 도달했다면
    if x >= 10:
        # 모든 1이 덮여있는지 확인
        for i in range(10):
            for j in range(10):
                if paper[i][j] == 1: # 덮지 못한 1이 있다면
                    return False
        # 모든 1을 덮었다면 최소값 갱신
        answer = min(answer, cnt)
        return
    
    # 다음 행으로 이동
    if y >= 10:
        dfs(x + 1, 0, cnt)
        return
    
    # 현재 위치가 1이라면 색종이를 놓아봄
    if paper[x][y] == 1:
        # 큰 색종이부터 시도
        for size in range(4, -1, -1):
            if remain[size] > 0:
                if check(x, y, size + 1): # 놓을 수 있다면
                    remain[size] -= 1 # 색종이 사용
                    put(x, y, size + 1, 0) # 색종이 놓기
                    dfs(x, y + 1, cnt + 1) # 다음 위치로 이동하고
                    remain[size] += 1 # 색종이 제거
                    put(x, y, size + 1, 1) # 원상복구
    else:
        dfs(x, y + 1, cnt) # 다음 위치로 이동
        
dfs(0,0,0)
print(-1 if answer == float('inf') else answer)