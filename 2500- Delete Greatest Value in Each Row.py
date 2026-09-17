class Solution(object):
    def deleteGreatestValue(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        ans = 0
        while len(grid[0]) != 0:
            x = 0
            for i in grid:
                if max(i) >= x:
                    x = max(i)
                i.remove(max(i))
            ans += x
        return ans