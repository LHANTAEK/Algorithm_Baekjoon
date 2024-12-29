import sys

lines = sys.stdin.readlines()

for line in lines:
    num = line.strip()
    if int(num) != 0:
        if num == num[::-1]:
            print("yes")
        else:
            print("no")
    else:
        break