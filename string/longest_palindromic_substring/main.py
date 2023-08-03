class Solution:

    def palindrome_expand(self, left, right, s):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    def longestPalindrome(self, s: str) -> str:
        ans = ''
        for i in range(len(s)):
            pal_odd = self.palindrome_expand(i, i, s)
            pal_even = self.palindrome_expand(i, i + 1, s)
            ans = max([ans, pal_odd, pal_even], key=len)
        return ans
