import sys
from itertools import combinations

input = sys.stdin.readline
nine_boys = sorted([int(input()) for _ in range(9)])

for i in combinations(nine_boys, 7):
    if sum(i) == 100:
        for j in i:
            print(j)
        break