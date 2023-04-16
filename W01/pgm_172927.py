# https://school.programmers.co.kr/learn/courses/30/lessons/172927

def cal_fatigue(picks, minerals, fatigue):
    dia = {"diamond": 1, "iron": 1, "stone": 1}
    iron = {"diamond": 5, "iron": 1, "stone": 1}
    stone = {"diamond": 25, "iron": 5, "stone": 1}
    min_fatigue = float("inf")
    
    if sum(picks) == 0 or len(minerals) == 0:
        return fatigue
    
    for i, f in enumerate((dia, iron, stone)):
        if picks[i] > 0:
            tmp = picks.copy()
            tmp[i] -= 1

            fatigue = cal_fatigue(tmp, minerals[5:], fatigue + sum(f[m] for m in minerals[:5]))
            min_fatigue = min(min_fatigue, fatigue)
    return min_fatigue

def solution(picks, minerals):
    return cal_fatigue(picks, minerals, 0)