class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        answer, temp = 0, 0
        for num in nums:
            if num == 1:
                temp += 1
                if answer < temp:
                    answer = temp
            else:
                temp = 0
        return answer