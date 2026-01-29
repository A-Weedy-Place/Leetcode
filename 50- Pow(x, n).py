class Solution(object):
    def myPow(self, x, n):
        if n == 0:
            return 1
        elif n < 0:
            x = 1/x
            n = -n

        ans = 1.0

        while n > 0:
            if n % 2 != 0:   # if n is odd
                ans *= x
                n -= 1       # make it even

            x = x * x        # square
            n = n // 2       # shrink exponent
        return ans