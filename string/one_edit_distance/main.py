class Solution:
    def is_one_edit_distance(self, s: str, t: str) -> bool:
        if len(s) == len(t):
            count_of_differences = 0
            for i in range(len(s)):
                if s[i] != t[i]:
                    count_of_differences += 1
            return count_of_differences == 1
        if len(s) == len(t) + 1:
            for i in range(len(s)):
                if t == s[0:i] + s[i + 1:]:
                    return True
        if len(s) == len(t) - 1:
            for i in range(len(t)):
                if s == t[0:i] + t[i + 1:]:
                    return True
        return False

print(Solution().is_one_edit_distance("ab", "ab"))