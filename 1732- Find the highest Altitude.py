class Solution(object):
    def largestAltitude(self, gain):
        """
        :type gain: List[int]
        :rtype: int
        """
        a = [0]
        for i in gain:
            a.append(a[-1] + i)
        return max(a)