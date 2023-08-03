class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        left = 0
        right = 1
        ans = 1
        while right < len(s):
            if s[right] in s[left:right]:
                ans = max(ans, right - left)
                left += s[left:right].index(s[right]) + 1
            right += 1
        ans = max(ans, right - left)
        return ans

s = "au"
print(Solution().lengthOfLongestSubstring(s))