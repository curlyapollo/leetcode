from typing import List

# идея: нам нужно найти левый и правый индекс минимального массива, при сортировке которого будет отсортирован весь массив
# в отсортированном массиве, если идти слева направо, максимум будет обновляться каждый раз
# если идти справа налево минимум будет обновляться каждый раз, тогда последнее обновление максимума – это правая граница
# последнее обновление минимума – левая
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        left = len(nums)
        mx = -1e6
        right = -1
        mn = 1e6
        for i in range(len(nums)):
            if nums[i] >= mx:
                mx = nums[i]
            else:
                right = i
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] <= mn:
                mn = nums[i]
            else:
                left = i
        return max(0, right - left + 1)