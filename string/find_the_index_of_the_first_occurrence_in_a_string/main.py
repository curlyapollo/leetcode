class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if len(needle) > len(haystack):
            return -1
        i = 0
        while i + len(needle) <= len(haystack):
            if haystack[i:i + len(needle)] == needle:
                return i
            i += 1
        return -1

haystack = "a"
needle = "a"
print(Solution().strStr(haystack, needle))