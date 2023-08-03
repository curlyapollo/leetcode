class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        left = 0
        right = len(s1) - 1
        hash_s1 = [0 for i in range(26)]
        for el in s1:
            hash_s1[ord(el) - ord('a')] += 1
        while right < len(s2):
            hash_sub = [0 for i in range(26)]
            for el in s2[left:right + 1]:
                hash_sub[ord(el) - ord('a')] += 1
            if hash_sub == hash_s1:
                return True
            left += 1
            right += 1
        return False

print(Solution().checkInclusion("ab", "eidbaooo"))