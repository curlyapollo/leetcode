class Solution:
    def maxPower(self, s: str) -> int:
        ans = 0
        cnt = 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                cnt += 1
            else:
                ans = max(cnt, ans)
                cnt = 1
        return max(ans, cnt)
