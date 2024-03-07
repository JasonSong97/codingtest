class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        answer = 0
        for num in nums:
            numberString = len(str(num))
            if numberString % 2 == 0:
                answer += 1
            else:
                continue
        return answer