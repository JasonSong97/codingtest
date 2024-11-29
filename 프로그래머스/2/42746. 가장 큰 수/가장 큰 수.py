# 가장 큰 수 구하기
# [6, 10, 2] -> [6102, 6210, 1062, 1026, 2610, 2106] -> 3!개수 -> 6102 (가장 큼)
# 1 <= len(numbers) <= 10만
# 0 <= 원소 <= 1000

# [3, 30, 34, 5, 9] -> 5! -> 120개
def solution(numbers):
    zeroCount = 0
    for n in numbers:
        if n == 0:
            zeroCount += 1
    if zeroCount == len(numbers):
        return "0"
    
    temp = list(map(str, numbers))
    temp.sort(key = lambda x: x * 3)
    answer = ''
    for i in range(len(temp) - 1, -1, -1):
        answer += temp[i]
    
    return answer