# https://school.programmers.co.kr/learn/courses/30/lessons/176962

def solution(plans):
    answer = []
    plans.sort(key = lambda x: x[1])
    
    for plan in plans:
        time = list(map(int, plan[1].split(':')))
        plan[1] = time[0]*60 + time[1] # start
        plan[2] = int(plan[2])         # playtime

    stop = []  # 중단된 과제 
    
    for plan in plans:
        name, start, play = plan
        
        while stop and stop[-1][1] <= start:
            answer.append(stop.pop()[0])
        stop.append([name, start])
        
        for s in stop: 
            s[1] += play
    
    answer.extend(list(s[0] for s in stop[::-1]))
    return answer