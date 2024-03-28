class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        # solution 1
        pointer = 0
        length = len(arr)
        while (pointer < length):
            if arr[pointer] == 0:
                arr.pop()
                arr.insert(pointer, 0)
                pointer += 1
            pointer += 1
        
        # # solution 2
        # zeroes = arr.count(0)
        # n = len(arr)
        # for i in range(n-1, -1, -1):
        #     if i + zeroes < n:
        #         arr[i + zeroes] = arr[i]
        #     if arr[i] == 0: 
        #         zeroes -= 1
        #         if i + zeroes < n:
        #             arr[i + zeroes] = 0
