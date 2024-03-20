class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        writePointer = 1
        for readPointer in range(1, len(nums)):
            if nums[readPointer - 1] != nums[readPointer]:
                nums[writePointer] = nums[readPointer]
                writePointer += 1
        return writePointer
                