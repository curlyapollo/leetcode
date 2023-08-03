from typing import List


class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        hist_a = [0] * (len(A) + 1)
        hist_b = [0] * (len(A) + 1)
        ans = [0] * (len(A) + 1)
        for i in range(len(A)):
            hist_a[A[i]] += 1
            hist_b[B[i]] += 1
            ans[i + 1] = ans[i]
            if A[i] == B[i]:
                ans[i + 1] += 1
            else:
                if hist_a[A[i]] == hist_b[A[i]]:
                    ans[i + 1] += 1
                if hist_a[B[i]] == hist_b[B[i]]:
                    ans[i + 1] += 1
        return ans[1:]
