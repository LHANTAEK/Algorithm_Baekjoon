# strip 메서드는 문자열 양쪽 끝의 불필요한 공백을 없애준다.
a, b = map(int, input().strip().split(' '))
c = a + b
print(f"{a} + {b} = {c}")
