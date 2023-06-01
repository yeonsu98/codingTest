# https://school.programmers.co.kr/learn/courses/30/lessons/150368

def off_cases(lst):
    cases = []
    for li in lst: # [[]]
        for n in [40, 30, 20, 10]:
            cases.append(li + [n]) # [[40],[30],[20],[10]]
    return cases

def solution(users, emoticons):

    cases = [[]]  # 이모티콘별 할인율 경우의 수
    for _ in range(len(emoticons)):
        cases = off_cases(cases)
    print(cases)
    # cases = [[40, 40],[40, 30],[40, 20],[10]]
    # [[40, 40], [40, 30], [40, 20], [40, 10], [30, 40], [30, 30], [30, 20], [30, 10], [20, 40], [20, 30], [20, 20], [20, 10], [10, 40], [10, 30], [10, 20], [10, 10]]
    answer_price = 0
    answer_user = 0
    for case in cases:
        user, p = 0, 0
        for off, price in users:
            cost = 0
            price = sum(map(lambda x: x[1] * (100 - x[0]) // 100, filter(lambda x: x[0] >= off, zip(case, emoticons))))
                
            for i in range(len(emoticons)):
                if case[i] >= off: 
                    cost += emoticons[i] * (100 - case[i]) // 100
            if cost >= price:
                user += 1
            else:
                p += cost
       
        answer_user, answer_price = max([answer_user, answer_price], [user, p])

    return answer_user, answer_price

# [1,3,4,2,6,5,9] : sort - nlogn
# [1,3,4,2,6,5,9] : max - n : heap

# [1,2,3,4]
# ...
# [1,2,3,4]
# [1,2,4,3]
# [1,3,2,4]
# [1,3,4,2]

solution([[40, 10000], [25, 10000]], [7000, 9000])

def test(): # return [1,2,3]
    yield 1
    yield 2
    yield 3

def test2():
    yield from test()

def main():
    for i in test2():
        print(i)

# [1,2,3,4], >> [1,2,3,4],[1,2,4,3],[1,3,2,4],....

[2,4,1,3]

def permutation(lst, prefix=[]):# lst: [1,2,3,4]
    if not lst:
        yield prefix
        return
    for i, el in enumerate(lst):
        yield from permutation(lst[:i] + lst[i+1:], prefix + [el])

# [1,2,3,4]
# yield from permutation([2,3,4],[1])
    # yield from permutation([3,4],[1,2])
        # yield from permutation([4],[1,2,3])
            # permutation([],[1,2,3,4])
        # yield from permutation([3],[1,2,4])
            # permutation([],[1,2,4,3])

    # yield from permutation([2,4],[1,3])
    # yield from permutation([2,3],[1,4])

# permutation([1,3,4],[2])
# permutation([1,2,4],[3])
# permutation([1,2,3],[4])

# [(할인율, 할인된 가격)]
# [7000, 9000]
# [[(10,6300),(10,9000)],[(10,7000),(20,9000)],[(10,7000),(30,9000)],[(10,7000),(40,9000)],[(20,7000),(10,9000)]

def permutation(price, prefix=[]): # [7000, 9000]
    if not price:
        yield prefix
        return
    
    for off in [10, 20, 30, 40]:
        for i, el in enumerate(price):
            el *= (100 - off) // 100
            yield from permutation(price[:i] + price[i+1:], prefix + [(off, el)])
# [(10,6300),(10,9000)]

lst = [4,3,2,1]
lst.sort()  # 리턴 값 X, 기존 값 바뀜
sorted(lst) # 리턴 값 O, 기존 값 안바뀜