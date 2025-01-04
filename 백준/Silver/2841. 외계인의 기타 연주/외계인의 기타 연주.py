import sys

input = sys.stdin.readline

N, P = map(int, input().split())
P_list =[i for i in range(1, P+1)]
lines = sys.stdin.readlines()
answer_dic = {}
cnt = 0

# N개를 돌아다니면서 키값 리스트 쌍을 딕셔너리에 추가
for line in lines:
    a, b = map(int, line.split())
    
    if str(a) not in answer_dic:
        answer_dic[str(a)] = [b]
        cnt += 1
        
    else:
        if answer_dic[str(a)][-1] < b: 
            cnt += 1
            answer_dic[str(a)].append(b)
        
        if answer_dic[str(a)][-1] > b:    
            while True:
                if answer_dic[str(a)] and answer_dic[str(a)][-1] > b:
                    cnt += 1
                    answer_dic[str(a)].pop()
                else:
                    if answer_dic[str(a)] and answer_dic[str(a)][-1] == b:
                        break
                    else:
                        cnt += 1
                        answer_dic[str(a)].append(b)

print(cnt)