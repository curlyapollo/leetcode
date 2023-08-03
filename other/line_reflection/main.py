from typing import (
    List,
)


class Solution:
    """
    @param points: n points on a 2D plane
    @return: if there is such a line parallel to y-axis that reflect the given points
    """

    def is_reflected(self, points: List[List[int]]) -> bool:
        mapa = {}
        points.sort()
        if len(points) % 2 == 1:
            x = points[len(points) // 2][0]
        else:
            x = (points[len(points) // 2 - 1][0] + points[len(points) // 2][0]) / 2
        for el in points:
            if el[1] in mapa.keys():
                mapa[el[1]] += el[0] - x
            else:
                mapa[el[1]] = el[0] - x
            if mapa[el[1]] == 0:
                mapa.pop(el[1])
        return len(mapa) == 0


c = Solution()
print(c.is_reflected([[1, 1], [-1, -1]]))
