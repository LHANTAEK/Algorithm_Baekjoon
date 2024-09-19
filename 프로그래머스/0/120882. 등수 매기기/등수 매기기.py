def solution(score):
    answer = []
    averages = [(s[0] + s[1])/2 for s in score]
    i_averages = [(avg, i) for i, avg in enumerate(averages)]
    i_averages.sort(key=lambda x: (-x[0],x[1]))
    ranks = [0] * len(score)
    
    rank = 1
    for i in range(len(i_averages)):
        if i > 0 and i_averages[i][0] == i_averages[i-1][0]:
            ranks[i_averages[i][1]] = ranks[i_averages[i-1][1]]
        else:
            ranks[i_averages[i][1]] = rank
        rank += 1
    return ranks