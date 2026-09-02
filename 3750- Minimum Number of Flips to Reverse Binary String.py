class Solution(object):
    def minimumFlips(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = bin(n)[2::]
        y = bin(n)[:1:-1]

        ans = 0

        for i in range(len(x)):
            if x[i] != y[i]:
                ans += 1
        
        return ans