class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        ans = 0
        distincts = 0
        hist = {}
        while j < len(s):
            if s[j] in hist:
                hist[s[j]] += 1
            else:
                hist[s[j]] = 1
                distincts += 1
            while distincts > 2:
                hist[s[i]] -= 1
                if hist[s[i]] == 0:
                    hist.pop(s[i])
                    distincts -= 1
                i += 1
            ans = max(ans, j - i + 1)
            j += 1
        return ans


print(Solution().lengthOfLongestSubstring("ccaabbb"))
