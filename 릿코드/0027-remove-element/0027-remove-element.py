class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        writePointer = 0
        for readPointer in range(len(nums)):
            # If read != val, 
            if nums[readPointer] != val:
                # index read value move to write index 
                nums[writePointer] = nums[readPointer]
                writePointer += 1

        return writePointer