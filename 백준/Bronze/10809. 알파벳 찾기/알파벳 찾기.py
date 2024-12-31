S = input()
alphabet = [chr(i) for i in range(97, 123)]

for l in range(len(S)):
    for i in range(len(alphabet)): # 입력된 단어를 순회
        if S[l] == alphabet[i]: # 입력된 단어의 알파벳이 알파벳 배열에 있으면
            alphabet[i] = l    # 단어의 알파벳 인덱스 번호를 똑같은 알파벳에 할당

for k in range(len(alphabet)):
    if type(alphabet[k]) == str:
        alphabet[k] = -1

print(' '.join(list(map(str, alphabet))))  