from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[left] < nums[right]:
                return nums[0]
            if nums[left] < nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        return nums[mid]