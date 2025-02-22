import sys
input = sys.stdin.readline

N, M = map(int, input().split())
program = {}

for _ in range(N):
    site, password = input().split()
    program[site] = password
    
for _ in range(M):
    site = input().strip()
    print(program[site])