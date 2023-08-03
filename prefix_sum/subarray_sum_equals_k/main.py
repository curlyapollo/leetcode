from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        pref_sum = 0
        dict = {0:1}
        for el in nums:
            pref_sum += el
            if pref_sum - k in dict:
                res += dict[pref_sum - k]
            if pref_sum in dict:
                dict[pref_sum] += 1
            else:
                dict[pref_sum] = 1
        return res