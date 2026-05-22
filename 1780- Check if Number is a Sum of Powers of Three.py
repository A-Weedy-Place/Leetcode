class Solution(object):
    def checkPowersOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        ans = []

        while n > 0:
            i = 0

            while 3 ** i <= n:
                i += 1

            power = i - 1
            ans.append(power)
            n -= 3 ** power

        return len(ans) == len(set(ans))