from typing import List


class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last = {}
        for i in range(len(s)):
            last[s[i]] = i
        left = right = 0
        ans = []
        for i in range(len(s)):
            right = max(right, last[s[i]])
            if i == right:
                ans.append(right - left + 1)
                left = i + 1
        return ans
