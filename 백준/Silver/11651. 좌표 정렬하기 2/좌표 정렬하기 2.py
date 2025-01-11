import sys
_ = input()
lines = sys.stdin.readlines()
result = []

for line in lines:
    result.append(list(map(int, line.split())))
    
result = sorted(result, key= lambda x: (x[1], x[0]))
    
for i in result:
    a, b = i[0], i[1]
    print(a, b, end='\n')