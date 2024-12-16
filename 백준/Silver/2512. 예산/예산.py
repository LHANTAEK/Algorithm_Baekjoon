# Step 1: 입력 받기
N = int(input().strip())             # 지방의 수
requests = list(map(int, input().split()))  # 각 지방의 요청 예산
M = int(input().strip())             # 총 예산

# Step 2: 요청들 중 최댓값과 요청들의 총합 계산
max_request = max(requests)   # 요청들 중 최댓값
total_request = sum(requests) # 요청들 합

# Step 3: 모든 요청의 합이 총 예산보다 작거나 같으면
# 상한액은 최대 요청 금액이 된다.
if total_request <= M:
    # 모든 요청을 그대로 배정 가능하므로 최대 요청액이 정답
    print(max_request)
    exit()

# Step 4: 이분 탐색을 위한 범위 설정
# 상한액의 최소값은 1원, 최대값은 최대 요청액에서 시작
start = 1
end = max_request
result = 0  # 결과(최대 상한액)를 저장할 변수

# Step 5: 이분 탐색 수행
while start <= end:
    mid = (start + end) // 2  # 상한액 후보(중간값)
    
    # 현재 상한액(mid)으로 배정했을 때 총 예산 사용량 계산
    current_sum = 0
    for r in requests:
        # 각 요청액 r이 상한액 mid를 넘으면 mid만 배정
        # 아니면 r 그대로 배정
        current_sum += min(r, mid)
    
    # 만약 이렇게 배정했을 때 총합이 예산 M을 넘는다면
    # 상한액(mid)을 낮춰서 예산 절감을 해야 한다.
    if current_sum > M:
        end = mid - 1
    else:
        # 총합이 M 이하라면, 더 늘릴 여지가 있다.
        # 현재 mid가 가능하므로 result에 저장하고
        # 상한액 범위를 더 높여본다.
        result = mid
        start = mid + 1

# Step 6: 최종적으로 탐색된 최대 상한액 출력
print(result)
