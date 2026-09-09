class Solution(object):
    def islandPerimeter(self, grid):
        ans = 0

        rows = len(grid)
        cols = len(grid[0])

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 1:
                    if i == 0 or grid[i-1][j] == 0:
                        ans += 1
                    if j == 0 or grid[i][j-1] == 0:
                        ans += 1
                    if i == rows-1 or grid[i+1][j] == 0:
                        ans += 1
                    if j == cols-1 or grid[i][j+1] == 0:
                        ans += 1
        return ans