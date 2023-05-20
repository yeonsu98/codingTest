# https://school.programmers.co.kr/learn/courses/30/lessons/150368

def off_cases(lst):
    cases = []
    for li in lst:
        for n in [40, 30, 20, 10]:
            cases.append(li + [n])
    return cases

def solution(users, emoticons):
    answer = []

    cases = [[]]  # 이모티콘별 할인율 경우의 수
    for _ in range(len(emoticons)):
        cases = off_cases(cases)

    for case in cases:
        result = [0, 0]
        for off, price in users:
            cost = 0
            for i in range(len(emoticons)):
                if case[i] >= off: 
                    cost += emoticons[i] * (100 - case[i]) // 100
            if cost >= price:
                result[0] += 1
            else:
                result[1] += cost
        answer.append(result)

    answer.sort(key=lambda x:(-x[0], -x[1]))
    return answer[0]

# [1,2,3,4]
# ...
# [1,2,3,4]
# [1,2,4,3]
# [1,3,2,4]
# [1,3,4,2]