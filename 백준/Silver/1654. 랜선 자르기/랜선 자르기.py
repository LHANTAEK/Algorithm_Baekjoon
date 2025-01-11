import sys
input = sys.stdin.readline

# 입력 처리
K, N = map(int, input().split())
K_list = [int(input()) for _ in range(K)]

# 이분 탐색 범위 설정
start, end = 1, max(K_list)  # 최소 길이는 1, 최대 길이는 가장 긴 랜선

# 이분 탐색
max_length = 0
while start <= end:
    mid = (start + end) // 2  # 현재 랜선 길이
    total = sum(k // mid for k in K_list)  # mid 길이로 잘랐을 때 랜선 개수
    
    if total >= N:  # 랜선 개수가 N 이상이면 길이를 더 늘릴 수 있음
        max_length = mid  # 현재 길이 저장
        start = mid + 1  # 더 긴 길이를 시도
    else:  # 랜선 개수가 부족하면 길이를 줄임
        end = mid - 1

print(max_length)