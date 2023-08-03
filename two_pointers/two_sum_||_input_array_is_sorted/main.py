from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        while i < j:
            if numbers[i] + numbers[j] == target:
                return [i, j]
            if numbers[i] + numbers[j] < target:
                i += 1
            else:
                j -= 1