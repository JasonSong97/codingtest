class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        length = len(arr)
        pointer = 0

        while pointer + 1 < length and arr[pointer] < arr[pointer + 1]:
            pointer += 1
        
        if pointer == 0 or pointer == length - 1:
            return False
        while pointer + 1 < length and arr[pointer] > arr[pointer + 1]:
            pointer += 1
        return length - 1 == pointer