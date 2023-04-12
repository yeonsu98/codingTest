# https://school.programmers.co.kr/learn/courses/30/lessons/178870

def solution(sequence, k):
    answer = []
    slen = len(sequence)
    ssum = 0
    l = 0
    r = -1
    
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
            answer.append([l, r])
            
    answer.sort(key=lambda x:(x[1]-x[0]))
    return answer[0]