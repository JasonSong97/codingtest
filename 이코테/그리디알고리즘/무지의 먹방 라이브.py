import heapq

def solution(food_times, k):
    if sum(food_times) <= k:
        return -1
    
    queueList = []
    for i in range(len(food_times)):
        heapq.heappush(queueList, (food_times[i], i + 1))
        
        # [8, 7, 5] 18
        # (5, 1) (7, 2) (8, 3) 18 > 15
        # (7, 2) (8, 3) 3 < 4
        # 
    
    sumValue = 0
    previous = 0
    length = len(food_times)

    while sumValue + ((queueList[0][0] - previous) * length) <= k:
        now = heapq.heappop(queueList)[0]
        sumValue += (now - previous) * length
        length -= 1
        previous = now
    
    answer = sorted(queueList, key = lambda x : x[1])
    return answer[(k - sumValue) % length][1]