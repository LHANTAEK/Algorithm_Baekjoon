N = int(input())

layer = 1 # 중심에서의 거리
count = 1 # 방번호   

while count < N: 
    count += 6 * layer # 각 layer마다 방의 개수는 6의 배수
    layer += 1
    
print(layer) 