def solution(emergency):
    answer = [0] * len(emergency)
    tempArr = sorted(emergency , reverse=True)
    count = 0
    for t in tempArr: # 76 24 3
        for i in range(len(emergency)): # [3, 76, 24]
            if t == emergency[i]:
                count += 1
                answer[i] += count
    return answer