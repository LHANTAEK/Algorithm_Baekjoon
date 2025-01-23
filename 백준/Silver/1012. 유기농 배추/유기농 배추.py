import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
test_num = int(input())

def dfs(x, y):
    board[x][y] = 0 # 방문처리
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx < M and 0 <= ny < N and board[nx][ny] == 1:
            dfs(nx, ny)

for _ in range(test_num):
    M, N, K = map(int, input().split())
    cnt = 0 # 지렁이 마리 수

    # 배추 공간 초기화
    board = [[0] * N for _ in range(M)]

    for _ in range(K):
        x, y = map(int, input().split())
        board[x][y] = 1
        
    # 배추 공간 순회
    for i in range(M):
        for j in range(N):
            # 배추가 심어져 있으면
            if board[i][j]:
                dfs(i,j)
                cnt += 1
    print(cnt)