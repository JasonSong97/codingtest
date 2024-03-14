class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        answer = 0
        for num in nums:
            numLength = len(str(num))
            if numLength % 2 == 0:
                answer += 1
            else:
                continue
        return answer