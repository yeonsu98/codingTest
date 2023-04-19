# https://school.programmers.co.kr/learn/courses/30/lessons/176962

def solution(plans):
    answer = []
    plans.sort(key = lambda x: x[1])
    
    for plan in plans:
        time = list(map(int, plan[1].split(':')))
        plan[1] = time[0]*60 + time[1] # start
        plan[2] = int(plan[2])         # playtime

    stop = []             # 중단된 과제 
    current = plans[0][1] # 현재 시간
    
    for i in range(len(plans)-1):
        np, _, tp = plans.pop(0)
        stop.append([np, tp])
        
        while stop:
            ns, ts = stop.pop()
            if current + ts <= plans[0][1]:
                answer.append(ns)
                current += ts
            else:
                res = (current + ts) - plans[0][1] # 남은 시간
                current += ts - res
                stop.append([ns, res])
                break
        
    answer.append(plans[-1][0])
    answer.extend(list(s[0] for s in stop[::-1]))
    return answer