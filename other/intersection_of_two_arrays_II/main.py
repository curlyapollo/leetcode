from typing import List


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        ans = []
        dict = {}
        for el in nums1:
            if el in dict:
                dict[el] += 1
            else:
                dict[el] = 1
        for el in nums2:
            if el in dict and dict[el] > 0:
                ans.append(el)
                dict[el] -= 1
        return ans