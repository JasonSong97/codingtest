# 장군개미 5 / 병정개미 3 / 일개미 1
def solution(hp):
    data = [5, 3, 1]
    answer = 0
    for d in data:
        answer += (hp // d)
        hp %= d
    return answer