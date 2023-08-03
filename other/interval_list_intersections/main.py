from typing import List


class Solution:
    def intersection(self, i1, i2):
        low = max(i1[0], i2[0])
        high = min(i1[1], i2[1])
        if low > high:
            return [high]
        return [low, high]

    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        i = j = 0
        ans = []
        while i < len(firstList) and j < len(secondList):
            inter = self.intersection(firstList[i], secondList[j])
            if len(inter) > 1:
                ans.append(inter)
            if secondList[j][1] > inter[-1]:
                i += 1
            else:
                j += 1
        return ans

first = [[0,2],[5,10],[13,23],[24,25]]
sec = [[1,5],[8,12],[15,24],[25,26]]
print(Solution().intervalIntersection(first, sec))
