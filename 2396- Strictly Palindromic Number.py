class Solution(object):
    def isStrictlyPalindromic(self, n):
        """
        :type n: int
        :rtype: bool
        """
        for i in range(2,n-1):
            x = []
            b = n

            while b > 0:
                x.append(b % i)
                b //= i

            for i in range(len(x)//2):
                if x[i] != x[-i-1]:
                    return False
        return True

# best sol is just return flase since every 4 or bigger is false but meh this is the solution ig