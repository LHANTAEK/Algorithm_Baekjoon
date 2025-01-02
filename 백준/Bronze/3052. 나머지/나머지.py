import sys

lines = sys.stdin.readlines()
answer = []

for line in lines:
    answer.append(int(line) % 42)
    
print(len(set(answer)))