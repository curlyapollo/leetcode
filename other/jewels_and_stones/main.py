class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        ans = 0
        for el in stones:
            ans += el in jewels
        return ans