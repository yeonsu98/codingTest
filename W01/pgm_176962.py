# https://school.programmers.co.kr/learn/courses/30/lessons/176962

def solution(plans):
    answer = []
    plans.sort(key = lambda x: x[1])
    stop = []
    
    for plan in plans:
        time = list(map(int, plan[1].split(':')))
        plan[1] = time[0]*60 + time[1] 
        plan[2] = int(plan[2])
        
    while plans:
        if len(plans) > 1:
            n1, s1, p1 = plans[0]
            n2, s2, p2 = plans[1]
            
            t1 = s1 + p1
            t2 = s2
            
            if t1 > t2: # 현재 과제 중단 stop에 추가
                stop.append([t1 - t2, n1])
                plans.pop(0)
            else: # 현재 과제 끝
                answer.append(n1)
                plans.pop(0)
                res = t2 - t1
                
                while stop: # stop한 과제 재개
                    print(stop)
                    if res >= stop[-1][0]: 
                        res -= stop[-1][0]
                        answer.append(stop.pop()[1])
                    else:
                        stop[-1][0] -= res
                        break
        else:
            answer.append(plans.pop(0)[0])
    
    stop.sort(reverse=True)
    for s in stop:
        answer.append(s[1])

    return answer