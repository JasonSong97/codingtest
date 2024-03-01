import time
import resource
import sys

def memory_usage():
    usage = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss
    if sys.platform == 'darwin':
        # macOS
        return usage / 1024.0 / 1024.0  # KB 단위를 MB로 변환

start_time = time.time()
start_memory_usage = memory_usage()

# 코딩 테스트 코드 시작
data = input()
result = int(data[0])

for i in range(1, len(data)):
    if int(data[i]) <= 1 or result <= 1:
        result += int(data[i])
    else:
        result *= int(data[i])

print('정답:', result)
# 코딩 테스트 코드 끝

end_memory_usage = memory_usage()
end_time = time.time()
execution_time_ms = (end_time - start_time) * 1000

memory_usage_MB = end_memory_usage - start_memory_usage
print("메모리 사용량: {:.2f} MB".format(memory_usage_MB))
print("실행 시간(ms): {:.2f} ms".format(execution_time_ms))