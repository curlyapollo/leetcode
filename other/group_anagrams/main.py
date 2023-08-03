from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict = {}
        ans = []
        for el in strs:
            key = ''.join(sorted(list(el)))
            if key in dict:
                dict[key].append(el)
            else:
                dict[key] = [el]
        for key in dict:
            ans.append(dict[key])
        return ans

print(Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"]))