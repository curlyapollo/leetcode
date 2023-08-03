from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        pref = [0 for i in range(len(nums) + 1)]
        remains = [0 for i in range(k)]
        for i in range(len(nums)):
            pref[i + 1] = pref[i] + nums[i]
            remains[pref[i + 1] % k] += 1
        ans = remains[0] * (remains[0] + 1) // 2
        for i in range(1, k):
            if remains[i] > 1:
                ans += remains[i] * (remains[i] - 1) // 2
        return ans

print(Solution().subarraysDivByK([8, 9, 7, 8, 9], 8))