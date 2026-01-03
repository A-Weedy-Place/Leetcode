class Solution(object):
    def findChampion(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        x = len(grid)
        arr = [0]*x
        for i in range(x):
            for j in range(x):
                if grid[i][j] == 1:
                    arr[i] += 1
        return arr.index(max(arr))