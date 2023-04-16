# Week 1

# https://school.programmers.co.kr/learn/courses/30/lessons/161989

def solution(n, m, section):
    answer = 0
    painted = 0

    for s in section:
        if s >= painted:
            painted = s + m
            answer += 1
            
    return answer

# https://school.programmers.co.kr/learn/courses/30/lessons/159994

def solution(cards1, cards2, goal):
    idx1 = idx2 = 0

    for g in goal:
        if (idx1 < len(cards1)) and cards1[idx1] == g:
            idx1 += 1
        elif (idx2 < len(cards2)) and cards2[idx2] == g:
            idx2 += 1
        else: 
            return 'No'

    return 'Yes'
# O(n)으로 풀 수 있도록 수정

# https://school.programmers.co.kr/learn/courses/30/lessons/155652

def solution(s, skip, index):
    answer = ''
    alpha = [chr(i) for i in range(ord('a'), ord('z')+1) if chr(i) not in skip]
    
    for c in s:
        answer += alpha[(alpha.index(c) + index) % len(alpha)]
        
    return answer
# 코드의 가독성 높이는 방향으로 짜기 !

# https://school.programmers.co.kr/learn/courses/30/lessons/147355

def solution(t, p):
    answer = 0
    tmp = 0
    
    for i in range(len(t)-len(p)+1):
        tmp = int(t[i:i+len(p)])
        
        if tmp <= int(p):
            answer += 1
        
    return answer

# https://school.programmers.co.kr/learn/courses/30/lessons/150370

def solution(today, terms, privacies):
    import datetime
    from dateutil.relativedelta import relativedelta
    
    format = '%Y.%m.%d'
    today_date = datetime.datetime.strptime(today, format)
    answer = []
    
    term = dict()
    for ts in terms:
        t = ts.split()
        term[t[0]] = t[1]
        
    for i, privacy in enumerate(privacies):
        p = privacy.split()
        p_date = datetime.datetime.strptime(p[0], format)
        p_name = p[1]
        
        t_mon = int(term[p_name])
        
        if today_date >= p_date + relativedelta(months=t_mon):
            answer.append(i+1)
        
    return answer

# 라이브러리 사용하지 않고 풀기
def cal_day(date): # 전체 일 수 구하는 함수
    date_arr = list(map(int, date.split('.')))
    day = date_arr[0]*12*28 + date_arr[1]*28 + date_arr[2]
    return day

def solution(today, terms, privacies):
    answer = []
    t_day = cal_day(today)
    
    term = dict()
    for ts in terms:
        t = ts.split()
        term[t[0]] = int(t[1])
        
    for i, privacy in enumerate(privacies, 1):
        # enumerate(arg1, arg2) => arg2로 시작값 세팅
        p = privacy.split()
        p_day = cal_day(p[0])
        mon = term[p[1]]
        
        if t_day >= p_day + 28 * mon:
            answer.append(i)
            
    return answer
# 반복되는 과정은 함수로 따로 지정