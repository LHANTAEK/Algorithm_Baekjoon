import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(current, parent_node):
    parent[current] = parent_node  
    
    for next_node in graph[current]: 
        if parent[next_node] == 0:  
            dfs(next_node, current)

n = int(input())
graph = [[] for _ in range(n+1)]
parent = [0] * (n+1)

for _ in range(n-1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1, 0)  

for i in range(2, n+1): 
    print(parent[i])