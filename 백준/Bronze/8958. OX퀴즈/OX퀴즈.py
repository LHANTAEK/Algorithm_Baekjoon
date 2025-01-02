import sys

N = int(input())
lines = sys.stdin.readlines()
result = 0

for line in lines:
    answer = 0
    for i in line:
        if i == "O":
            result += 1
            answer += result
        else:
            result = 0
    print(answer)