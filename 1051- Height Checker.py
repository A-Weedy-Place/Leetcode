class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        b = 0
        a = sorted(heights)
        for x in range(len(heights)):
            if a[x] != heights[x]:
                b += 1
        return b