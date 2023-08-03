from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        ans, current_area = 0, 0
        while left <= right:
            current_area = min(height[left], height[right]) * (right - left)
            ans = max(ans, current_area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return ans