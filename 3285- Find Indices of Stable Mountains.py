class Solution(object):
    def stableMountains(self, height, threshold):
        """
        :type height: List[int]
        :type threshold: int
        :rtype: List[int]
        """
        x = []
        for i in range(len(height)-1):
            if height[i] > threshold:
                x.append(i+1)
        return x