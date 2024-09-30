from collections import deque

def solution(A, B):
    
    if A == B:
        return 0
    
    A = deque(A)
    
    for i in range(1, 1+len(A)):
        A.rotate(1)
        if B == ''.join(A):
            return i
    
    return -1