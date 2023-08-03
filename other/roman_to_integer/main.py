class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            el = s[i]
            if el == "M":
                ans += 1000
            elif el == "D":
                ans += 500
            elif el == "C":
                if i < len(s) - 1 and s[i + 1] in "DM":
                    ans -= 100
                else:
                    ans += 100
            elif el == "L":
                ans += 50
            elif el == "X":
                if i < len(s) - 1 and s[i + 1] in "LC":
                    ans -= 10
                else:
                    ans += 10
            elif el == "V":
                ans += 5
            else:
                if i < len(s) - 1 and s[i + 1] in "VX":
                    ans -= 1
                else:
                    ans += 1
        return ans