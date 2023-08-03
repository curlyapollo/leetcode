class Solution:
    def firstUniqChar(self, s: str) -> int:
        dict1 = {}
        for el in s:
            if el in dict1:
                dict1[el] += 1
            else:
                dict1[el] = 1
        for i in range(len(s)):
            if dict1[s[i]] == 1:
                return i
        return -1