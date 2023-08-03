from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        closest = 1e9
        for i in range(len(nums) - 2):
            j = i + 1
            k = len(nums) - 1
            while j < k:
                sum = nums[i] + nums[j] + nums[k]
                if sum < target:
                    j += 1
                else:
                    k -= 1
                if abs(sum - target) < abs(closest - target):
                    closest = sum
        return closest