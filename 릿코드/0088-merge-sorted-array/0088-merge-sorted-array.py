class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        # 1 two pointer start from the end
        # time complexity: O(n + m)
        # space complexity: O(1)
        # pointer1 = m - 1 # 2
        # pointer2 = n - 1 # 2

        # for pointer3 in range(n + m - 1, -1, -1):
        #     if pointer2 < 0:
        #         break

        #     if pointer1 >= 0 and nums1[pointer1] > nums2[pointer2]:
        #         nums1[pointer3] = nums1[pointer1]
        #         pointer1 -= 1
        #     else:
        #         nums1[pointer3] = nums2[pointer2]
        #         pointer2 -= 1
        
        # 2 two pointer start from the beginning
        # time complexity: O(n + m)
        # space complexity: O(n)
        nums1Copy = nums1[:m]
        pointer1 = 0
        pointer2 = 0

        for pointer3 in range(n + m):
            if n <= pointer2 or (pointer1 < m and nums1Copy[pointer1] <= nums2[pointer2]):
                nums1[pointer3] = nums1Copy[pointer1]
                pointer1 += 1
            else:
                nums1[pointer3] = nums2[pointer2]
                pointer2 += 1

        # 3 merge and sort
        # time complexity: O(n + m)
        # space complexity: O(n)
        # for i in range(n):
        #     nums1[i + m] = nums2[i]
        
        # nums1.sort()