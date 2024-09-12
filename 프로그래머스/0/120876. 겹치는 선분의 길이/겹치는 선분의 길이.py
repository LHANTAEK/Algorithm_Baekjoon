def solution(lines):
    answer = 0
    answer_list = []
    
    for i in lines:
        a, b = i
        answer_list.append(list(range(a, b)))
        
    q, w, e = answer_list
    
    # if len(set(q) & set(w)) > 0:
    #     answer = len(set(q) & set(w)) 
    # elif len(set(q) & set(e)) > 0:
    #     answer = len(set(q) & set(e))
    # elif len(set(w) & set(e)) > 0:
    #     answer = len(set(w) & set(e))
    # else:
    #     answer = 0
    
    if len((set(q) & set(w)) | (set(q) & set(e)) | (set(w) & set(e))):
        answer = len((set(q) & set(w)) | (set(q) & set(e)) | (set(w) & set(e)))
    else:
        answer = 0
    
    return answer