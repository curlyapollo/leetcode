from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = 0
        right = n - 1
        k = n - 1
        ans = [0] * n
        while k >= 0:
            if abs(nums[left]) > abs(nums[right]):
                ans[k] = nums[left] ** 2
                left += 1
            else:
                ans[k] = nums[right] ** 2
                right -= 1
        return ans