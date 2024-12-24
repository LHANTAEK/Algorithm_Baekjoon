import sys


lines = sys.stdin.readlines()
numbers = [int(line.strip()) for line in lines]

max_num = max(numbers)

for i in range(len(numbers)):
    if numbers[i] == max_num:
        print(numbers[i])
        print(i+1)