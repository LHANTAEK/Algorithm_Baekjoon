def solution(id_pw, db):
    answer = ''
    for idi_pw in db:
        idi, pw = idi_pw
        if idi in id_pw:
            if pw in id_pw:
                return 'login'
            else:
                return 'wrong pw'
        
    return 'fail'