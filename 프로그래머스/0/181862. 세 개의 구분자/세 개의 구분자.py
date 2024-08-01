
def solution(myStr):
    import re
    answer = []
    result = re.split(r'[abc]', myStr)
    for i in result:
        if i:
            answer.append(i)
    if not answer:
        answer.append('EMPTY')
    
    return answer