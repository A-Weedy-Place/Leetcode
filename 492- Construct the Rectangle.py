class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        x = int(area ** (0.5))

        if x*x != area:
            x += 1

        for i in range(x, area+1):
            if area % i == 0:
                x = i
                break
        
        return [x,area/x]