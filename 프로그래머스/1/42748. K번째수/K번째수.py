# 자르고 -> 정렬 -> k 번째 수 구하기
# [1, 5, 2, 6, 3, 7, 4] -> [5, 2, 6, 3] -> 정렬 [2, 3, 5, 6] -> 3번째 수 5
def solution(array, commands):
    answer = []
    for arr in commands:
        i = arr[0] - 1
        j = arr[1]
        temp = array[i: j] # [5, 2, 6, 3]
        temp.sort()
        answer.append(temp[arr[2] - 1])
    return answer