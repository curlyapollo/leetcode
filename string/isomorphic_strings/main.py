class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        dict1, dict2 = {}, {}
        for i in range(len(s)):
            if s[i] in dict1:
                if t[i] != dict1[s[i]]:
                    return False
            else:
                if t[i] in dict2:
                    return False
                dict1[s[i]] = t[i]
                dict2[t[i]] = s[i]
        return True


Solution().isIsomorphic("egg", "add")