# class Solution:
#     def checkIfExist(self, arr: List[int]) -> bool:
#         for i in range(len(arr)):
#             temp1 = arr[i]
#             multi = temp1 * 2
#             devide = temp1 / 2
#             if multi in arr:
#                 return True
#             if devide and multi in arr:
#                 return True

#         return False
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = set()
        for num in arr:
            if num * 2 in seen or (num % 2 == 0 and num // 2 in seen):
                return True
            seen.add(num)
        return False
