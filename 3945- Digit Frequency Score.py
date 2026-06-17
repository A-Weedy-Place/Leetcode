class Solution(object):
    def digitFrequencyScore(self, n):
        """
        :type n: int
        :rtype: int
        """
        s = str(n)
        ans = 0

        for d in set(s):
            ans += int(d) * s.count(d)

        return ans