from typing import List, Tuple, Any


class Solution:

    def leftBinSearch(self, nums, target):
        left = 0
        right = len(nums) - 1
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                ans = mid
                right = mid - 1
        return ans

    def rightBinSearch(self, nums, target):
        left = 0
        right = len(nums) - 1
        ans = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                ans = mid
                left = mid + 1
        return ans

    def searchRange(self, nums: List[int], target: int):
        return self.leftBinSearch(nums, target), self.rightBinSearch(nums, target)

nums = [5,7,7,8,8,10]
print(Solution().leftBinSearch(nums, 8))