# https://school.programmers.co.kr/learn/courses/30/lessons/154538

def solution(x, y, n):

    s = set()
    s.add(x)
    
    answer = 0

    while s:
        if y in s: # 변환 완료
            return answer
        
        nxt_cal = set()
        for i in s:
            if i+n <= y:
                nxt_cal.add(i+n)
            if i*2 <= y:
                nxt_cal.add(i*2)
            if i*3 <= y:
                nxt_cal.add(i*3)
                
        s = nxt_cal
        answer+=1
        
    return -1