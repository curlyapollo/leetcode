from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) * len(matrix[0]) - 1
        while left <= right:
            mid = (left + right) // 2
            num_mid = matrix[mid // len(matrix)][mid % len(matrix)]
            if num_mid == target:
                return True
            elif num_mid < target:
                left = mid + 1
            else:
                right = mid - 1
        return False