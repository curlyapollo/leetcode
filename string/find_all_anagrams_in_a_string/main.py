from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        p_dict = {}
        for el in p:
            if el in p_dict:
                p_dict[el] += 1
            else:
                p_dict[el] = 1
        sub_dict = {}
        for el in s[:len(p)]:
            if el in sub_dict:
                sub_dict[el] += 1
            else:
                sub_dict[el] = 1
        i = 0
        j = len(p) - 1
        ans = []
        while j < len(s):
            if i > 0:
                if sub_dict[s[i - 1]] == 1:
                    sub_dict.pop(s[i - 1])
                else:
                    sub_dict[s[i - 1]] -= 1
                if s[j] in sub_dict:
                    sub_dict[s[j]] += 1
                else:
                    sub_dict[s[j]] = 1
            if p_dict == sub_dict:
                ans.append(i)
            i += 1
            j += 1
        return ans


s = "cbaebabacd"
p = "abc"
Solution().findAnagrams(s, p)