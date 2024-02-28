import psutil
import time
import sys

start_time = time.time()
start_memory_usage = psutil.Process().memory_info().rss
input = sys.stdin.readline

# 코딩 테스트 코드 시작
n = int(input())
dataList = list(map(int, input().split()))
result = 0

dataList.sort()

count = 0
for data in dataList:
     count += 1
     if count >= data:
          count = 0
          result += 1
          continue

print('정답:', result)
# 코딩 테스트 코드 끝

end_memory_usage = psutil.Process().memory_info().rss
end_time = time.time()
execution_time_ms = (end_time - start_time) * 1000

memory_usage_MB = (end_memory_usage - start_memory_usage) / (1024 * 1024)
print("메모리 사용량: {} MB".format(memory_usage_MB))
print("실행 시간(ms): {:.2f} ms".format(execution_time_ms))