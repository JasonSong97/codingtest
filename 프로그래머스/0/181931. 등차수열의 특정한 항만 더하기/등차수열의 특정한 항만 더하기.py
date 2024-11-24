# a = a1 + (n - 1)d
def solution(a, d, included):
    answer = 0
    for i in range(len(included)):
        if included[i]:
            answer += (a + ((i + 1) - 1) * d)
    return answer