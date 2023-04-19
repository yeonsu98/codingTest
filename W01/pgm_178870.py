# https://school.programmers.co.kr/learn/courses/30/lessons/178870

def solution(sequence, k):
    slen = len(sequence)
    ssum = 0
    l = 0
    r = -1
    answer = [0, float("inf")]
    
    while True:
        if ssum < k:
            r += 1
            if r >= slen:
                break
            else:
                ssum += sequence[r]
        else:
            ssum -= sequence[l]
            if l >= slen:
                break
            l += 1

        if ssum == k:
            if answer[1]-answer[0] > r-l:
                answer = [l, r]
            
    return answer