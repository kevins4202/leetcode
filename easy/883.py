class Solution:
    def projectionArea(self, grid: List[List[int]]) -> int:
        ans = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 0: ans += 1
        for i in range(len(grid)):
            ans += max(grid[i])

        for i in range(len(grid[0])):
            ans += max([l[i] for l in grid])

        return ans