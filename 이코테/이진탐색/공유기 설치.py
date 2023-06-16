import sys

input = sys.stdin.readline
N, C = map(int, input().split()) # 5 3

data = []
for i in range(N):
    data.append(int(input()))
    
data.sort()
start = data[0] # 1
end = data[-1] - data[0] # 8
# 1 2 4 8 9
answer = 0
while start <= end:
    mid = (start + end) // 2 # 4 3
    value = data[0] # 1
    count = 1
    
    # 1 2 4 8 9
    for i in range(1, N):
        if data[i] >= mid + value:
            value = data[i]
            count += 1
    if count >= C:
        answer = mid
        start = mid + 1
    else:
        end = mid - 1
        
print(answer)
