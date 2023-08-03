from typing import List


class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        ans1 = []
        ans2 = []
        for el in nums1:
            if el not in nums2 and el not in ans1:
                ans1.append(el)
        for el in nums2:
            if el not in nums1 and el not in ans2:
                ans2.append(el)
        return [ans1, ans2]