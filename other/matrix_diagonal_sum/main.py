from typing import List


class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        ans = 0
        for i in range(len(mat)):
            ans += mat[i][i]
            if i != len(mat) - i - 1:
                ans += mat[i][len(mat) - i - 1]
        return ans
