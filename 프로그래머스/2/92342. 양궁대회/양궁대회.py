from itertools import combinations_with_replacement

def solution(n, info):
    max_diff = 0
    best_comb = [-1]

    # 가능한 모든 화살의 배치 경우의 수를 계산
    for comb in combinations_with_replacement(range(11), n):
        ryan_info = [0] * 11
        for i in comb:
            ryan_info[10 - i] += 1

        # 라이언과 어피치의 점수 계산
        ryan_score, apeach_score = 0, 0
        for i in range(11):
            if info[i] == 0 and ryan_info[i] == 0:
                continue
            if ryan_info[i] > info[i]:
                ryan_score += 10 - i
            else:
                apeach_score += 10 - i

        # 점수 차이가 더 크고 라이언이 우승할 수 있는 경우 결과 갱신
        diff = ryan_score - apeach_score
        if diff > max_diff:
            max_diff = diff
            best_comb = ryan_info

    return best_comb