import sys

input = sys.stdin.readline

N = int(input().strip()) # 지방의 수
requests = list(map(int, input().split())) # 각 지방의 요청 예산
M = int(input().strip()) # 총 예산

max_request = max(requests) # 요청들 중 최댓값
total_request = sum(requests) # 요청들 합

if total_request <= M:
    print(max_request)
    exit()

start = 1
end = max_request
result = 0 # 결과(최대 상한액)를 저장할 변수

while start <= end:
    mid = (start + end) // 2 # 상한액 후보(중간값)
    
    current_sum = 0
    for r in requests:
        current_sum += min(r, mid)
        
    if current_sum > M:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
        
print(result)