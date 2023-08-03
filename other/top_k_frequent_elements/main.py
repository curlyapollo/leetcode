from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dict1 = {}
        for el in nums:
            if el in dict1:
                dict1[el] += 1
            else:
                dict1[el] = 1
        barrier = sorted(dict1.values(), reverse=True)[k - 1]
        ans = []
        for el in dict1:
            if dict1[el] >= barrier:
                ans.append(el)
        return ans