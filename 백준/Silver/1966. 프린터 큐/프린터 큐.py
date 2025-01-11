from collections import deque

testcase = int(input())

for _ in range(testcase):
    ans = deque()
    N, M = map(int, input().split())
    doc = list(map(int, input().split()))
    
    # M은 인덱스를 의미하므로 언제 나오는지 확인하기 위해서
    for index, priority in enumerate(doc):
       ans.append([priority, index])    
    
    # 우선순위대로 나오는 로직 구현
    count = 0
    max_priority = max(ans, key=lambda x: x[0])[0] # 초기 최대 우선순위
    
    while ans:
        if ans[0][0] == max_priority:
            popped = ans.popleft()
            count += 1
            
            if popped[1] == M: # result 반환
                print(count)
                break
            
            if ans: # 비어있지 않으면 최대 우선순위 갱신
                max_priority = max(ans, key=lambda x: x[0])[0]
        else:
            ans.append(ans.popleft())