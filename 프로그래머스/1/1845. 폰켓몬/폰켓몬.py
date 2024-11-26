# n마리 중에서 n/2마리 가져가셈
# 종류에 따라 번호 부여 -> 같은 종류는 같은 번호
# EX) 4마리 -> [3, 1, 2, 3] -> 3번 2마리 + 1번 1마리 + 2번 1마리
# 4마리 중에서 2마리 고르는 케이스
# 1. (3[1번째], 1)
# 2. (3[1번째], 2)
# 3. (3[1번째], 3[4번쨰])
# 4. (1, 2)
# 5. (1, 3[4번째])
# 6. (2, 3[4번째])
# => 3번의 경우는 동일한 것으로 취급 따라서 2종류가 가장 많음
def solution(nums):
    targetCount = len(nums) // 2
    answer = set(nums)
    if len(answer) <= targetCount:
        return len(answer)
    else:
        return targetCount