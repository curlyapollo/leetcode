from typing import List


class Solution:
    def dfs(self, i, j, grid, used):
        if grid[i][j] == '1' and (i, j) not in used:
            used.add((i, j))
            if i > 0:
                self.dfs(i - 1, j, grid, used)
            if i < len(grid) - 1:
                self.dfs(i + 1, j, grid, used)
            if j > 0:
                self.dfs(i, j - 1, grid, used)
            if j < len(grid[0]) - 1:
                self.dfs(i, j + 1, grid, used)

    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        ans = 0
        used = set()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i, j) not in used:
                    ans += 1
                    self.dfs(i, j, grid, used)
        return ans


grid1 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
print(Solution().numIslands(grid1))