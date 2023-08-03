from typing import List


class Solution:
    # у нас идея: перебирать места обрывов столбцов это a-й столбец, для этого m + 1 в height,
    # чтобы последний обрывающий столбец был уже вне, и мы считали всю матрицу
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        cols = len(matrix[0])
        height = [0] * (cols + 1)
        res = 0
        for row in matrix:
            for i in range(cols):
                if row[i] == "1":
                    height[i] += 1
                else:
                    height[i] = 0
            stack = [-1]
            for a in range(cols + 1):
                # удаляем столбцы до нас больше нас
                # в стеке только возрастающий порядок, тк добавляя новый столбец, удаляем все, больше него
                # по асимптотике: мы один раз добавляем и один раз удаляем каждый столбец
                while height[a] < height[stack[-1]]:
                    h = height[stack.pop()]
                    w = a - stack[-1] - 1
                    res = max(res, h * w)
                stack.append(a)
        return res

# асимптотика O(mn), так как в среднем вайл работает два раза, так как один раз удаляем, один раз добавляем

matrix = [["1", "0"], ["1", "0"],["1", "0"],["1", "0"],["1", "0"],["1", "0"],["1", "0"],["1", "0"],["1", "1"], ["1", "1"]]
print(Solution().maximalRectangle(matrix))