import sys

x = sys.stdin.readlines()

for i in x:
    a, b, c = map(int, i.strip().split())
    if a + b + c != 0:
        if a**2 + b**2 == c**2:
            print("right")
        elif a**2 + c**2 == b**2:
            print("right")
        elif b**2 + c**2 == a**2:
            print("right")
        else:
            print("wrong")
    else:
        break