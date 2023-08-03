class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0] * 26
        for x in s:
            count[ord(x) - ord('a')] += 1
        for x in t:
            count[ord(x) - ord('a')] -= 1
        for val in count:
            if val != 0:
                return False
        return True