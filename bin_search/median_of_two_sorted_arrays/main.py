from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # nums1 должно быть меньше, так как по нему будем делать бинпоиск
        if len(nums1) >= len(nums2):
            nums1, nums2 = nums2, nums1
        n, m = len(nums1), len(nums2)
        total_len = n + m
        half = total_len // 2

        # бинпоиск по меньшему массиву
        left, right = 0, n - 1
        while True:
            mid1 = (left + right) // 2
            mid2 = half - mid1 - 2
            # теперь найдем 4 значения возле каждой серединки
            if mid1 >= 0:
                left_by_mid1 = nums1[mid1]
            else:
                left_by_mid1 = float("-inf")
            if mid1 < n - 1:
                right_by_mid1 = nums1[mid1 + 1]
            else:
                right_by_mid1 = float("+inf")
            if mid2 >= 0:
                left_by_mid2 = nums2[mid2]
            else:
                left_by_mid2 = float("-inf")
            if mid2 < m - 1:
                right_by_mid2 = nums2[mid2 + 1]
            else:
                right_by_mid2 = float("+inf")
            if left_by_mid1 <= right_by_mid2 and left_by_mid2 <= right_by_mid1:
                if total_len % 2 == 0:
                    return (max(left_by_mid1, left_by_mid2) + min(right_by_mid1, right_by_mid2)) / 2
                else:
                    return min(right_by_mid1, right_by_mid2)
            else:
                if left_by_mid1 > right_by_mid2:
                    right = mid1 - 1
                else:
                    left = mid1 + 1


print(Solution().findMedianSortedArrays([], [1]))