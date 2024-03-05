class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []

        temp = 0
        for num in nums:
            temp += num
            result.append(temp)
        return result