class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        answer = 0
        for i in range(len(nums)):
            if len(str(nums[i])) % 2 == 0:
                answer += 1
        return answer