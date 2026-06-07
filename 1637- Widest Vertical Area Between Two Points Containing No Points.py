class Solution(object):
    def maxWidthOfVerticalArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        x = [i[0] for i in points]
        # x = list(set(x))
        # Damn i though removing the repeated entries would decrease loop and make it faster but apparently not?
        x.sort()
        ans = 0
        for i in range(len(x)-1):
            if x[i+1] - x[i] > ans:
                ans = x[i+1] - x[i]
        return ans     