import sys
from itertools import combinations
input = sys.stdin.readline
N, M = map(int, input().split())

# 0은 빈곳, 1은 집, 2는 치킨집
map = [list(map(int, input().split())) for _ in range(N)]

# 행열을 돌아다니면서 집과 치킨집에 해당하는 좌표(1부터 시작)를 각각의 리스트에 추가
home = []
chicken = []

for i in range(N):
    for j in range(N):
        if map[i][j] == 1:
            home.append([i+1, j+1])
        if map[i][j] == 2:
            chicken.append([i+1, j+1])

# 2(치킨집)를 최대 M으로 했을 때 고르는 경우의 수 생성
chicken_combs = list(combinations(chicken, M))

# 각각의 집 좌표를 순회하면서 max_chicken 안에 있는 좌표와 거리를 비교 후 최단거리값 계산 후 리스트에 저장
# 치킨집 조합에 대한 집 좌표간의 거리 최소값 설정
min_city_dist = float('inf')

# 치킨집 좌표 순회
# 최대 치킨집 조합을 순회
for comb in chicken_combs:
    # 치킨집 조합에 대한 집 간 최단 거리를 위한 설정
    city_dist = 0
    
    # 집 좌표 순회
    for h in home:
        # 치킨집과 집 최소값을 위한 값 설정
        min_dist = float('inf')
        
    # 조합 중에서 치킨집 좌표를 순회
        for c in comb:
            dist = abs(h[0] - c[0]) + abs(h[1] - c[1])
            min_dist = min(min_dist, dist)
        city_dist += min_dist
    min_city_dist = min(min_city_dist, city_dist)


# 최소값 출력
print(min_city_dist)