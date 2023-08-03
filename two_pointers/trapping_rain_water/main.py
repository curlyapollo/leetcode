from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        i = 0
        j = len(height) - 1
        max_unit = 0
        while i <= j:
            min_unit = min(height[i], height[j])
            # максимум из минимумов, которые прошли
            # максимум всегда слево от i, так как если справа от j, то мы бы не сдвигали j налево, ведь двигаем только когда меньше
            max_unit = max(max_unit, min_unit)
            ans += max_unit - min_unit
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
        return ans

print(Solution().trap([0,1,0,2,1,0,1,3,2,1,2,1]))