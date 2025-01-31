from collections import deque

def bfs(n, k):
    q = deque()
    q.append(n)
    visited = [-1] * 100001
    visited[n] = 0
    
    while q:
        x = q.popleft()
        
        # 동생 위치 도달
        if x == k: 
            return visited[x]
        
        for nx in (x-1, x+1, x*2):
            if 0 <= nx <= 100000 and visited[nx] == -1: # 범위 내이고 미방문일 때
                visited[nx] = visited[x] + 1
                q.append(nx)
                
n, k = map(int, input().split())
print(bfs(n, k))