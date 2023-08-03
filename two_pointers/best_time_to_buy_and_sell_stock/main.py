from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 0
        j = 0
        ans = 0
        while j < len(prices):
            ans = max(ans, prices[j] - prices[i])
            if prices[j] < prices[i]:
                i = j
            j += 1
        return ans