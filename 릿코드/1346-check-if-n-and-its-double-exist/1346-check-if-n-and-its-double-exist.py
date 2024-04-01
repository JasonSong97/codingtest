class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for i in range(len(arr)):
            if arr[i] / 2 in arr or arr[i] * 2 in arr:
                if arr[i] / 2 == 0 or arr[i] * 2 == 0:
                    if arr.count(0) >= 2:
                        return True
                    continue
                
                return True
        return False