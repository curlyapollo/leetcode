import math
from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        ans = 0
        # при первом прохождении, когда встретим первую единицу distance = 2 * seats.index(1), так как прибавляем по единичке
        # поэтому ноормально делим на 2
        distance = seats.index(1)
        for seat in seats:
            if seat == 1:
                ans = max(ans, math.ceil(distance / 2))
                distance = 0
            else:
                distance += 1
        return max(ans, distance)
