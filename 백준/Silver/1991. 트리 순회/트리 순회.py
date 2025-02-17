import sys
input = sys.stdin.readline

n = int(input())
tree = {}

# 트리 만들기
for _ in range(n):
    node, left, right = input().split()
    tree[node] = [left, right]

# 전위 순회: 루트 -> 왼쪽 -> 오른쪽
def preorder(node):
    if node == '.':  # 자식이 없는 경우
        return
    print(node, end='')  # 루트
    preorder(tree[node][0])  # 왼쪽
    preorder(tree[node][1])  # 오른쪽

# 중위 순회: 왼쪽 -> 루트 -> 오른쪽
def inorder(node):
    if node == '.':
        return
    inorder(tree[node][0])  # 왼쪽
    print(node, end='')  # 루트
    inorder(tree[node][1])  # 오른쪽

# 후위 순회: 왼쪽 -> 오른쪽 -> 루트
def postorder(node):
    if node == '.':
        return
    postorder(tree[node][0])  # 왼쪽
    postorder(tree[node][1])  # 오른쪽
    print(node, end='')  # 루트

# 각각의 순회 실행
preorder('A')
print()
inorder('A')
print()
postorder('A')