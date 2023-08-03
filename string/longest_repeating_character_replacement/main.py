class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 0:
            return 0
        hist = {}
        left = 0
        ans = 0
        for right in range(len(s)):
            if s[right] in hist:
                hist[s[right]] += 1
            else:
                hist[s[right]] = 1
            cur_letters = right - left + 1
            # здесь макс работает за O(26), так как букв максимально 26
            if cur_letters - max(hist.values()) <= k:
                ans = max(ans, cur_letters)
            else:
                hist[s[left]] -= 1
                left += 1
                # right -= 1
        return ans