_ = input()
A = list(map(int, input().split()))
_ = input()
B = list(map(int, input().split()))
diff = set(B) - set(A)

for i in B:
    if i in diff:
        print(0)
    else:
        print(1)