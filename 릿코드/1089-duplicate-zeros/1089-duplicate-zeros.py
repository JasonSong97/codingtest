class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        zeroCount = arr.count(0)
        length = len(arr)
        for i in range(length - 1, -1, -1):
            # 뒤로 순회
            if i + zeroCount < length:
                arr[i + zeroCount] = arr[i]
            if arr[i] == 0:
                zeroCount -= 1
                if i + zeroCount < length:
                    arr[i + zeroCount] = 0
            