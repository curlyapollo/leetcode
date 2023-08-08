class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)
        dict = {}
        left = 0
        ans = 1
        for right in range(len(s)):
            if s[right] in dict and dict[s[right]] >= left:
                ans = max(ans, right - left)
                left = dict[s[right]] + 1
            else:
                ans = max(ans, right - left + 1)
            dict[s[right]] = right
        return ans

s = "au"
print(Solution().lengthOfLongestSubstring(s))
