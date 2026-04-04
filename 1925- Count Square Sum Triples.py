class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        x = 0
        # for i in range(1,n+1):
        #     for j in range(1,n+1):
        #         for k in range(1,n+1):
        #             if i**2 + j**2 == k**2:
        #                 x += 1

        for i in range(1, n+1):
            for j in range(1, n+1):
                k2 = i*i + j*j
                k = int(k2 ** 0.5)
                if k*k == k2 and k <= n:
                    x += 1

        return x   