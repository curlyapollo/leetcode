from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = [1] * n
        pre = 1
        post = 1
        for i in range(n):
            ans[i] *= pre
            pre *= nums[i]
            ans[n - i - 1] *= post
            post *= nums[n - i - 1]
        return ans

nums = [1, 2, 3, 4]
print(Solution().productExceptSelf(nums))