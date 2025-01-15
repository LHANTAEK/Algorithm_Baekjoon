node = int(input())
edge = int(input())
graph = [[] for _ in range(node)]
visited = [0 for _ in range(node)]

def dfs(x):
    visited[x] = 1
    for i in graph[x]:
        if not visited[i]:
            dfs(i)

for _ in range(edge):
    a, b = map(lambda x: x-1, map(int, input().split()))
    graph[a].append(b)
    graph[b].append(a)

dfs(0)
print(sum(visited)-1)