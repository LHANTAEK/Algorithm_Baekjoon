import sys

input = sys.stdin.readline
book = {}

for i in range(int(input())):
    i = input()
    if i not in book:
        book[i] = 1
    else:
        book[i] += 1

book = sorted(book.items(), key = lambda x: (-x[1], x[0]))
print(book[0][0])