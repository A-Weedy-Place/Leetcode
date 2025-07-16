class Solution(object):
    def sumOfSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        a = 0
        for x in range(1, n+1):
            if n % x == 0:
                a = a + (nums[x-1]**2)
        return a 