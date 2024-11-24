def solution(arr, k):
    answer = []
    count = 0
    for i in range(len(arr)):
        if arr[i] not in answer:
            answer.append(arr[i])
            count += 1
            if count >= k:
                break
                
    if len(answer) < k:
        for _ in range(k - len(answer)):
            answer.append(-1)
    return answer